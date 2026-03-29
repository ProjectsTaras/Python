"""
Bird Species Classifier using TensorFlow
==========================================
Transfer learning with EfficientNetB0 to classify 1,486 bird species.
Uses pure TensorFlow APIs: tf.data pipelines, tf.image augmentation,
and a custom tf.GradientTape training loop.

Dataset: birds_train_small — 1,486 species, ~140 images each (~208K total).
Directory structure: archive/birds_train_small/<species_folder>/<image>.jpg

Usage:
    python bird_classifier.py                              # Train the model
    python bird_classifier.py --predict path/to/image.jpg  # Predict a single image
"""

import os
import sys
import json
import argparse
import tensorflow as tf

# ──────────────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "archive", "birds_train_small")
CHECKPOINT_DIR = os.path.join(BASE_DIR, "checkpoints")
SAVED_MODEL_DIR = os.path.join(BASE_DIR, "saved_model")
CLASS_NAMES_PATH = os.path.join(BASE_DIR, "class_names.json")

IMG_SIZE = 224
BATCH_SIZE = 32
VALIDATION_SPLIT = 0.2
SEED = 42

INITIAL_EPOCHS = 10     # Phase 1: train only the classification head
FINE_TUNE_EPOCHS = 10   # Phase 2: fine-tune top layers of the backbone
INITIAL_LR = 1e-3
FINE_TUNE_LR = 1e-5


def extract_species_name(folder_name):
    """Extract readable species name from folder name.

    Folder format: 03111_Animalia_Chordata_Aves_Order_Family_Genus_species
    Returns: 'Genus species'
    """
    parts = folder_name.split("_")
    if len(parts) >= 2:
        return f"{parts[-2]} {parts[-1]}"
    return folder_name


# ──────────────────────────────────────────────────────────────────────────────
# tf.data Pipeline
# ──────────────────────────────────────────────────────────────────────────────
def build_label_lookup(data_dir):
    """Build a class-name-to-integer lookup from the directory structure."""
    class_dirs = sorted([
        d for d in tf.io.gfile.listdir(data_dir)
        if tf.io.gfile.isdir(os.path.join(data_dir, d))
    ])
    num_classes = len(class_dirs)
    class_to_idx = {name: i for i, name in enumerate(class_dirs)}

    # Save human-readable species map
    species_map = {i: extract_species_name(name) for i, name in enumerate(class_dirs)}
    with open(CLASS_NAMES_PATH, "w") as f:
        json.dump(species_map, f, indent=2)

    print(f"Found {num_classes} bird species")
    print(f"Class names saved to: {CLASS_NAMES_PATH}")
    return class_to_idx, num_classes


def collect_file_paths_and_labels(data_dir, class_to_idx):
    """Walk the directory tree and collect (file_path, label) pairs."""
    paths, labels = [], []
    for class_name, label in class_to_idx.items():
        class_dir = os.path.join(data_dir, class_name)
        for fname in tf.io.gfile.listdir(class_dir):
            if fname.lower().endswith((".jpg", ".jpeg", ".png")):
                paths.append(os.path.join(class_dir, fname))
                labels.append(label)
    return paths, labels


def parse_image(file_path, label):
    """Read, decode and resize a single image using tf.io / tf.image."""
    raw = tf.io.read_file(file_path)
    image = tf.image.decode_jpeg(raw, channels=3)
    image = tf.image.resize(image, [IMG_SIZE, IMG_SIZE])
    image = tf.cast(image, tf.float32)
    return image, label


def augment(image, label):
    """Apply data augmentation using tf.image ops."""
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, max_delta=0.1)
    image = tf.image.random_contrast(image, lower=0.9, upper=1.1)
    image = tf.image.random_saturation(image, lower=0.9, upper=1.1)
    # Random rotation via a small angle
    angle = tf.random.uniform([], -0.15, 0.15)
    image = rotate_image(image, angle)
    image = tf.clip_by_value(image, 0.0, 255.0)
    return image, label


@tf.function
def rotate_image(image, angle):
    """Rotate image by angle (radians) using tf ops."""
    cos_a = tf.math.cos(angle)
    sin_a = tf.math.sin(angle)
    # Affine transform: [cos, -sin, 0, sin, cos, 0, 0, 0]
    transform = [cos_a, -sin_a, 0.0, sin_a, cos_a, 0.0, 0.0, 0.0]
    image = tf.expand_dims(image, 0)
    image = tf.raw_ops.ImageProjectiveTransformV3(
        images=image,
        transforms=tf.expand_dims(transform, 0),
        output_shape=tf.shape(image)[1:3],
        interpolation="BILINEAR",
        fill_mode="NEAREST",
        fill_value=0.0,
    )
    return tf.squeeze(image, 0)


def preprocess(image, label):
    """EfficientNet preprocessing: scale pixels to [0, 255] range
    (EfficientNet has its own internal normalization)."""
    return image, label


def create_datasets():
    """Build tf.data.Dataset pipelines for training and validation."""
    print(f"Loading images from: {DATA_DIR}")
    print(f"Image size: {IMG_SIZE}x{IMG_SIZE}, Batch size: {BATCH_SIZE}")

    class_to_idx, num_classes = build_label_lookup(DATA_DIR)
    paths, labels = collect_file_paths_and_labels(DATA_DIR, class_to_idx)

    total = len(paths)
    print(f"Total images: {total}")

    # Shuffle and split into train / val
    tf.random.set_seed(SEED)
    indices = tf.random.shuffle(tf.range(total), seed=SEED)
    split = int(total * (1 - VALIDATION_SPLIT))

    train_idx = indices[:split]
    val_idx = indices[split:]

    paths_t = tf.constant(paths)
    labels_t = tf.constant(labels, dtype=tf.int32)

    train_paths = tf.gather(paths_t, train_idx)
    train_labels = tf.gather(labels_t, train_idx)
    val_paths = tf.gather(paths_t, val_idx)
    val_labels = tf.gather(labels_t, val_idx)

    print(f"Training samples: {len(train_idx)}, Validation samples: {len(val_idx)}")

    autotune = tf.data.AUTOTUNE

    train_ds = (
        tf.data.Dataset.from_tensor_slices((train_paths, train_labels))
        .shuffle(buffer_size=min(len(train_idx), 10000), seed=SEED)
        .map(parse_image, num_parallel_calls=autotune)
        .map(augment, num_parallel_calls=autotune)
        .map(preprocess, num_parallel_calls=autotune)
        .batch(BATCH_SIZE)
        .prefetch(autotune)
    )

    val_ds = (
        tf.data.Dataset.from_tensor_slices((val_paths, val_labels))
        .map(parse_image, num_parallel_calls=autotune)
        .map(preprocess, num_parallel_calls=autotune)
        .batch(BATCH_SIZE)
        .prefetch(autotune)
    )

    return train_ds, val_ds, num_classes, len(train_idx)


# ──────────────────────────────────────────────────────────────────────────────
# Model (built with tf.keras layers, but trained with GradientTape)
# ──────────────────────────────────────────────────────────────────────────────
def build_model(num_classes):
    """Build an EfficientNetB0-based classifier."""
    base_model = tf.keras.applications.EfficientNetB0(
        include_top=False,
        weights="imagenet",
        input_shape=(IMG_SIZE, IMG_SIZE, 3),
    )
    base_model.trainable = False  # Freeze for Phase 1

    inputs = tf.keras.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
    # EfficientNet includes its own preprocessing layer internally
    x = base_model(inputs, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Dropout(0.3)(x)
    x = tf.keras.layers.Dense(512, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.3)(x)
    outputs = tf.keras.layers.Dense(num_classes)(x)  # raw logits

    model = tf.keras.Model(inputs, outputs, name="bird_classifier")
    return model, base_model


# ──────────────────────────────────────────────────────────────────────────────
# Custom Training Loop with tf.GradientTape
# ──────────────────────────────────────────────────────────────────────────────
@tf.function
def train_step(model, images, labels, optimizer, loss_fn, train_loss, train_acc):
    """Single training step."""
    with tf.GradientTape() as tape:
        logits = model(images, training=True)
        loss = loss_fn(labels, logits)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    train_loss.update_state(loss)
    train_acc.update_state(labels, logits)


@tf.function
def val_step(model, images, labels, loss_fn, val_loss, val_acc):
    """Single validation step."""
    logits = model(images, training=False)
    loss = loss_fn(labels, logits)
    val_loss.update_state(loss)
    val_acc.update_state(labels, logits)


def run_epoch(model, dataset, optimizer, loss_fn, metrics, training=True):
    """Run one epoch of training or validation."""
    loss_metric, acc_metric = metrics
    loss_metric.reset_state()
    acc_metric.reset_state()

    for images, labels in dataset:
        if training:
            train_step(model, images, labels, optimizer, loss_fn,
                       loss_metric, acc_metric)
        else:
            val_step(model, images, labels, loss_fn,
                     loss_metric, acc_metric)

    return loss_metric.result().numpy(), acc_metric.result().numpy()


def train():
    """Full training pipeline with custom tf.GradientTape loop."""
    train_ds, val_ds, num_classes, num_train = create_datasets()
    model, base_model = build_model(num_classes)

    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

    # Metrics
    train_loss = tf.keras.metrics.Mean(name="train_loss")
    train_acc = tf.keras.metrics.SparseCategoricalAccuracy(name="train_acc")
    val_loss_metric = tf.keras.metrics.Mean(name="val_loss")
    val_acc_metric = tf.keras.metrics.SparseCategoricalAccuracy(name="val_acc")

    # Checkpoint manager
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)

    model.summary()

    best_val_acc = 0.0
    patience_counter = 0

    # ── Phase 1: Train classification head (base model frozen) ───────────
    print("\n" + "=" * 60)
    print("Phase 1: Training classification head (base model frozen)")
    print("=" * 60)

    optimizer = tf.keras.optimizers.Adam(learning_rate=INITIAL_LR)
    lr_var = optimizer.learning_rate

    for epoch in range(1, INITIAL_EPOCHS + 1):
        t_loss, t_acc = run_epoch(
            model, train_ds, optimizer, loss_fn,
            (train_loss, train_acc), training=True
        )
        v_loss, v_acc = run_epoch(
            model, val_ds, None, loss_fn,
            (val_loss_metric, val_acc_metric), training=False
        )

        print(f"Epoch {epoch}/{INITIAL_EPOCHS} — "
              f"loss: {t_loss:.4f}, acc: {t_acc:.4f} — "
              f"val_loss: {v_loss:.4f}, val_acc: {v_acc:.4f} — "
              f"lr: {float(lr_var):.2e}")

        # Manual early stopping + LR reduction
        if v_acc > best_val_acc:
            best_val_acc = v_acc
            patience_counter = 0
            # Save best checkpoint
            ckpt = tf.train.Checkpoint(model=model, optimizer=optimizer)
            ckpt.write(os.path.join(CHECKPOINT_DIR, "phase1_best"))
        else:
            patience_counter += 1
            if patience_counter >= 2:
                new_lr = max(float(lr_var) * 0.5, 1e-6)
                lr_var.assign(new_lr)
                print(f"  ReduceLR -> {new_lr:.2e}")
            if patience_counter >= 3:
                print("  Early stopping triggered")
                # Restore best weights
                ckpt = tf.train.Checkpoint(model=model, optimizer=optimizer)
                ckpt.read(os.path.join(CHECKPOINT_DIR, "phase1_best"))
                break

    phase1_epochs = min(epoch, INITIAL_EPOCHS)

    # ── Phase 2: Fine-tune top layers of EfficientNetB0 ──────────────────
    print("\n" + "=" * 60)
    print("Phase 2: Fine-tuning top layers of EfficientNetB0")
    print("=" * 60)

    base_model.trainable = True
    fine_tune_from = int(len(base_model.layers) * 0.7)
    for layer in base_model.layers[:fine_tune_from]:
        layer.trainable = False

    trainable = sum(1 for l in base_model.layers if l.trainable)
    frozen = sum(1 for l in base_model.layers if not l.trainable)
    print(f"Base model: {trainable} trainable, {frozen} frozen layers")

    optimizer_ft = tf.keras.optimizers.Adam(learning_rate=FINE_TUNE_LR)
    lr_var_ft = optimizer_ft.learning_rate

    patience_counter = 0

    for epoch in range(1, FINE_TUNE_EPOCHS + 1):
        global_epoch = phase1_epochs + epoch

        t_loss, t_acc = run_epoch(
            model, train_ds, optimizer_ft, loss_fn,
            (train_loss, train_acc), training=True
        )
        v_loss, v_acc = run_epoch(
            model, val_ds, None, loss_fn,
            (val_loss_metric, val_acc_metric), training=False
        )

        print(f"Epoch {global_epoch}/{phase1_epochs + FINE_TUNE_EPOCHS} — "
              f"loss: {t_loss:.4f}, acc: {t_acc:.4f} — "
              f"val_loss: {v_loss:.4f}, val_acc: {v_acc:.4f} — "
              f"lr: {float(lr_var_ft):.2e}")

        if v_acc > best_val_acc:
            best_val_acc = v_acc
            patience_counter = 0
            ckpt = tf.train.Checkpoint(model=model, optimizer=optimizer_ft)
            ckpt.write(os.path.join(CHECKPOINT_DIR, "phase2_best"))
            print(f"  Saved best checkpoint (val_acc: {v_acc:.4f})")
        else:
            patience_counter += 1
            if patience_counter >= 2:
                new_lr = max(float(lr_var_ft) * 0.5, 1e-7)
                lr_var_ft.assign(new_lr)
                print(f"  ReduceLR -> {new_lr:.2e}")
            if patience_counter >= 5:
                print("  Early stopping triggered")
                ckpt = tf.train.Checkpoint(model=model, optimizer=optimizer_ft)
                ckpt.read(os.path.join(CHECKPOINT_DIR, "phase2_best"))
                break

    # Save as SavedModel format (pure TensorFlow, no Keras .keras file)
    print(f"\nSaving model to: {SAVED_MODEL_DIR}")
    tf.saved_model.save(model, SAVED_MODEL_DIR)
    print(f"Best validation accuracy: {best_val_acc:.4f}")

    return model


# ──────────────────────────────────────────────────────────────────────────────
# Prediction
# ──────────────────────────────────────────────────────────────────────────────
def predict(image_path, top_k=5):
    """Predict bird species for a given image using the saved TF model."""
    if not os.path.exists(SAVED_MODEL_DIR):
        print(f"Error: No trained model found at {SAVED_MODEL_DIR}")
        print("Run training first: python bird_classifier.py")
        sys.exit(1)

    if not os.path.exists(CLASS_NAMES_PATH):
        print(f"Error: Class names file not found at {CLASS_NAMES_PATH}")
        sys.exit(1)

    # Load SavedModel
    print(f"Loading model from: {SAVED_MODEL_DIR}")
    model = tf.saved_model.load(SAVED_MODEL_DIR)
    infer = model.signatures["serving_default"]

    with open(CLASS_NAMES_PATH) as f:
        species_map = json.load(f)

    # Load and preprocess image with tf.io / tf.image
    raw = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(raw, channels=3)
    image = tf.image.resize(image, [IMG_SIZE, IMG_SIZE])
    image = tf.cast(image, tf.float32)
    image = tf.expand_dims(image, 0)  # Add batch dimension

    # Run inference
    output = infer(image)
    # Get the output tensor (key name varies; take the first one)
    logits = list(output.values())[0]
    probs = tf.nn.softmax(logits, axis=-1).numpy()[0]

    top_indices = probs.argsort()[-top_k:][::-1]

    print(f"\nPredictions for: {image_path}")
    print("-" * 50)
    for i, idx in enumerate(top_indices, 1):
        species = species_map[str(idx)]
        confidence = probs[idx] * 100
        print(f"  {i}. {species:<30s} {confidence:6.2f}%")


# ──────────────────────────────────────────────────────────────────────────────
# Entry Point
# ──────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bird Species Classifier (TF)")
    parser.add_argument(
        "--predict", type=str, default=None,
        help="Path to an image to classify (skips training)",
    )
    parser.add_argument(
        "--top-k", type=int, default=5,
        help="Number of top predictions to show (default: 5)",
    )
    args = parser.parse_args()

    if args.predict:
        predict(args.predict, top_k=args.top_k)
    else:
        train()
