from pathlib import Path
from uuid import uuid4

from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(Path("static") / "uploads")

recipes = []


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/recipes")
def get_recipes():
    return jsonify(recipes)


@app.post("/api/recipes")
def create_recipe():
    dish_type = request.form.get("dish_type", "").strip()
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()

    if not dish_type or not title or not description:
        return jsonify({"error": "Заповніть обов'язкові поля."}), 400

    image_url = ""
    image_file = request.files.get("image")
    if image_file and image_file.filename:
        upload_dir = Path(app.config["UPLOAD_FOLDER"])
        upload_dir.mkdir(parents=True, exist_ok=True)
        filename = secure_filename(image_file.filename)
        unique_name = f"{uuid4().hex}_{filename}"
        save_path = upload_dir / unique_name
        image_file.save(save_path)
        image_url = f"/static/uploads/{unique_name}"

    recipe = {
        "dish_type": dish_type,
        "title": title,
        "description": description,
        "image_url": image_url,
    }
    recipes.insert(0, recipe)
    return jsonify(recipe), 201


if __name__ == "__main__":
    app.run(debug=True)
