const roles = {
  PlannerAgent: "Dzieli glowne zadanie na etapy",
  BenefitsAgent: "Zbiera argumenty za wdrozeniem",
  RisksAgent: "Analizuje ryzyka i ograniczenia",
  SafetyAgent: "Proponuje zasady bezpiecznego uzycia",
  DecisionAgent: "Laczy wyniki i tworzy rekomendacje",
};

const state = {
  data: null,
  currentStep: -1,
};

const elements = {
  runButton: document.getElementById("runButton"),
  nextButton: document.getElementById("nextButton"),
  resetButton: document.getElementById("resetButton"),
  scenarioTitle: document.getElementById("scenarioTitle"),
  scenarioGoal: document.getElementById("scenarioGoal"),
  scenarioContext: document.getElementById("scenarioContext"),
  agentsGrid: document.getElementById("agentsGrid"),
  timeline: document.getElementById("timeline"),
  stepCounter: document.getElementById("stepCounter"),
  activeAgent: document.getElementById("activeAgent"),
  detailTitle: document.getElementById("detailTitle"),
  detailContent: document.getElementById("detailContent"),
  agentStatus: document.getElementById("agentStatus"),
};

async function loadDemo() {
  const response = await fetch("/api/demo");
  if (!response.ok) {
    throw new Error("Nie udalo sie pobrac danych demonstracyjnych");
  }
  return response.json();
}

function renderScenario(scenario) {
  elements.scenarioTitle.textContent = scenario.title;
  elements.scenarioGoal.textContent = scenario.user_goal;
  elements.scenarioContext.textContent = scenario.context;
}

function renderAgents(steps) {
  elements.agentsGrid.innerHTML = "";
  for (const step of steps) {
    const card = document.createElement("article");
    card.className = "agent-card";
    card.dataset.agent = step.agent_name;
    card.innerHTML = `
      <h3 class="agent-name">${step.agent_name}</h3>
      <p class="agent-role">${roles[step.agent_name] || "Agent"}</p>
    `;
    elements.agentsGrid.appendChild(card);
  }
}

function renderTimeline(steps) {
  elements.timeline.innerHTML = "";
  steps.forEach((step, index) => {
    const item = document.createElement("article");
    item.className = "timeline-item";
    item.dataset.index = String(index);
    const inputs = step.inputs.length
      ? `Otrzymuje dane od: ${step.inputs.join(", ")}`
      : "Rozpoczyna prace od poczatkowego polecenia uzytkownika";
    item.innerHTML = `
      <strong>Krok ${index + 1}: ${step.agent_name}</strong>
      <p>${inputs}</p>
    `;
    elements.timeline.appendChild(item);
  });
}

function resetView() {
  state.currentStep = -1;
  elements.stepCounter.textContent = `0 / ${state.data.steps.length}`;
  elements.activeAgent.textContent = "Jeszcze nie uruchomiono";
  elements.detailTitle.textContent = "Kliknij \"Uruchom demonstracje\"";
  elements.detailContent.textContent = "Po starcie tutaj zobaczysz wynik pracy kazdego agenta.";
  elements.agentStatus.textContent = "Oczekiwanie";

  document.querySelectorAll(".agent-card").forEach((card) => {
    card.classList.remove("active", "done");
  });
  document.querySelectorAll(".timeline-item").forEach((item) => {
    item.classList.remove("active", "done");
  });

  elements.runButton.disabled = false;
  elements.nextButton.disabled = true;
  elements.resetButton.disabled = true;
}

function showStep(index) {
  state.currentStep = index;
  const step = state.data.steps[index];

  document.querySelectorAll(".agent-card").forEach((card) => {
    const isCurrent = card.dataset.agent === step.agent_name;
    const cardIndex = state.data.steps.findIndex((item) => item.agent_name === card.dataset.agent);
    card.classList.toggle("active", isCurrent);
    card.classList.toggle("done", cardIndex < index);
  });

  document.querySelectorAll(".timeline-item").forEach((item) => {
    const itemIndex = Number(item.dataset.index);
    item.classList.toggle("active", itemIndex === index);
    item.classList.toggle("done", itemIndex < index);
  });

  elements.stepCounter.textContent = `${index + 1} / ${state.data.steps.length}`;
  elements.activeAgent.textContent = step.agent_name;
  elements.detailTitle.textContent = step.title;
  elements.detailContent.textContent = step.content;
  elements.agentStatus.textContent =
    index === state.data.steps.length - 1 ? "Gotowe" : "Trwa wykonanie";

  elements.resetButton.disabled = false;
  elements.nextButton.disabled = index === state.data.steps.length - 1;
}

async function init() {
  try {
    state.data = await loadDemo();
    renderScenario(state.data.scenario);
    renderAgents(state.data.steps);
    renderTimeline(state.data.steps);
    resetView();
  } catch (error) {
    elements.detailTitle.textContent = "Nie udalo sie uruchomic demonstracji";
    elements.detailContent.textContent = String(error);
  }
}

elements.runButton.addEventListener("click", () => {
  showStep(0);
  elements.runButton.disabled = true;
  elements.nextButton.disabled = state.data.steps.length === 1;
});

elements.nextButton.addEventListener("click", () => {
  const nextIndex = state.currentStep + 1;
  if (nextIndex < state.data.steps.length) {
    showStep(nextIndex);
  }
});

elements.resetButton.addEventListener("click", resetView);

init();
