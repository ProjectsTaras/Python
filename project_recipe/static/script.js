const modal = document.getElementById("modal");
const openBtn = document.getElementById("openFormBtn");
const closeBtn = document.getElementById("closeFormBtn");
const form = document.getElementById("recipeForm");
const recipesEl = document.getElementById("recipes");

function openModal() {
  modal.classList.remove("hidden");
  modal.setAttribute("aria-hidden", "false");
}

function closeModal() {
  modal.classList.add("hidden");
  modal.setAttribute("aria-hidden", "true");
}

function renderRecipes(recipes) {
  recipesEl.innerHTML = "";

  if (!recipes.length) {
    recipesEl.innerHTML = "<p>Ще немає рецептів. Додайте перший.</p>";
    return;
  }

  recipes.forEach((recipe) => {
    const card = document.createElement("article");
    card.className = "card";
    card.innerHTML = `
      <h3>${recipe.title}</h3>
      <p><strong>Страва:</strong> ${recipe.dish_type}</p>
      <p>${recipe.description}</p>
      ${recipe.image_url ? `<img src="${recipe.image_url}" alt="${recipe.title}">` : ""}
    `;
    recipesEl.appendChild(card);
  });
}

async function loadRecipes() {
  const response = await fetch("/api/recipes");
  const recipes = await response.json();
  renderRecipes(recipes);
}

openBtn.addEventListener("click", openModal);
closeBtn.addEventListener("click", closeModal);

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(form);

  const response = await fetch("/api/recipes", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    const data = await response.json();
    alert(data.error || "Помилка при збереженні.");
    return;
  }

  form.reset();
  closeModal();
  loadRecipes();
});

window.addEventListener("click", (event) => {
  if (event.target === modal) {
    closeModal();
  }
});

loadRecipes();
