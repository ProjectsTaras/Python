from __future__ import annotations

from dataclasses import dataclass
from textwrap import fill
from typing import Any


WRAP_WIDTH = 90


@dataclass
class AgentMessage:
    agent_name: str
    title: str
    content: str


@dataclass
class LessonScenario:
    title: str
    user_goal: str
    context: str


class BaseAgent:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, scenario: LessonScenario, memory: list[AgentMessage]) -> AgentMessage:
        raise NotImplementedError


class PlannerAgent(BaseAgent):
    def run(self, scenario: LessonScenario, memory: list[AgentMessage]) -> AgentMessage:
        content = (
            f"Cel uzytkownika: {scenario.user_goal}\n"
            "Plan wspolpracy agentow:\n"
            "1. Zebrac argumenty za wdrozeniem AI-asystenta w szkole.\n"
            "2. Zebrac ryzyka i ograniczenia.\n"
            "3. Zaproponowac zasady bezpiecznego uzycia.\n"
            "4. Polaczyc wyniki i wydac rekomendacje dla dyrekcji szkoly."
        )
        return AgentMessage(self.name, "Podzial zadania", content)


class BenefitsAgent(BaseAgent):
    def run(self, scenario: LessonScenario, memory: list[AgentMessage]) -> AgentMessage:
        content = (
            "Najwazniejsze korzysci:\n"
            "- szybsze wyszukiwanie informacji i materialow do nauki;\n"
            "- pomoc w tlumaczeniu trudnych pojec i tworzeniu planu nauki;\n"
            "- wsparcie nauczyciela przy przygotowaniu cwiczen, quizow i podsumowan;\n"
            "- personalizacja pracy ucznia: rozne poziomy trudnosci i tempo nauki;\n"
            "- automatyzacja prostych zadan organizacyjnych, np. porzadkowanie notatek."
        )
        return AgentMessage(self.name, "Argumenty za", content)


class RisksAgent(BaseAgent):
    def run(self, scenario: LessonScenario, memory: list[AgentMessage]) -> AgentMessage:
        content = (
            "Najwazniejsze ryzyka:\n"
            "- bledne odpowiedzi lub zmyslone informacje;\n"
            "- zbyt duze zaufanie do AI i spadek samodzielnosci uczniow;\n"
            "- ryzyko plagiatu i bezrefleksyjnego kopiowania gotowych tresci;\n"
            "- problemy z prywatnoscia danych;\n"
            "- nierowny dostep do narzedzi cyfrowych i internetu."
        )
        return AgentMessage(self.name, "Ryzyka i ograniczenia", content)


class SafetyAgent(BaseAgent):
    def run(self, scenario: LessonScenario, memory: list[AgentMessage]) -> AgentMessage:
        content = (
            "Proponowane zasady wdrozenia:\n"
            "- AI ma wspierac nauke, a nie zastepowac myslenie ucznia;\n"
            "- kazda wazna informacje trzeba sprawdzic w drugim zrodle;\n"
            "- uczniowie powinni ujawniac, kiedy korzystali z AI przy pracy;\n"
            "- nie wolno wpisywac do systemu danych wrazliwych;\n"
            "- nauczyciel ustala, przy jakich zadaniach uzycie AI jest dozwolone."
        )
        return AgentMessage(self.name, "Zasady bezpiecznego uzycia", content)


class DecisionAgent(BaseAgent):
    def run(self, scenario: LessonScenario, memory: list[AgentMessage]) -> AgentMessage:
        benefits = next(msg for msg in memory if msg.agent_name == "BenefitsAgent")
        risks = next(msg for msg in memory if msg.agent_name == "RisksAgent")
        safety = next(msg for msg in memory if msg.agent_name == "SafetyAgent")

        content = (
            "Rekomendacja koncowa:\n"
            "Szkola powinna testowo wdrozyc AI-asystenta jako narzedzie wspierajace nauke, "
            "poniewaz korzysci edukacyjne sa wyrazne. Wdrozenie musi jednak obejmowac "
            "jasne zasady uzycia, kontrole nauczyciela i sprawdzanie wiarygodnosci odpowiedzi.\n\n"
            "Dlaczego to jest system agentowy, a nie jeden chatbot?\n"
            "- jeden agent planuje zadanie;\n"
            "- drugi zbiera argumenty za;\n"
            "- trzeci analizuje ryzyka;\n"
            "- czwarty proponuje zasady bezpieczenstwa;\n"
            "- piaty laczy wyniki i podejmuje decyzje.\n\n"
            "Wniosek dla uczniow:\n"
            "Agenci wspolpracuja, bo kazdy specjalizuje sie w innym fragmencie problemu. "
            "To pozwala lepiej kontrolowac proces i latwiej wychwycic bledy.\n\n"
            f"Wykorzystane wejscia:\n- {benefits.title}\n- {risks.title}\n- {safety.title}"
        )
        return AgentMessage(self.name, "Koncowa rekomendacja", content)


class MultiAgentLessonDemo:
    def __init__(self) -> None:
        self.agents = [
            PlannerAgent("PlannerAgent"),
            BenefitsAgent("BenefitsAgent"),
            RisksAgent("RisksAgent"),
            SafetyAgent("SafetyAgent"),
            DecisionAgent("DecisionAgent"),
        ]

    def run(self, scenario: LessonScenario) -> list[AgentMessage]:
        memory: list[AgentMessage] = []
        for agent in self.agents:
            memory.append(agent.run(scenario, memory))
        return memory

    def run_as_steps(self, scenario: LessonScenario) -> list[dict[str, Any]]:
        memory: list[AgentMessage] = []
        steps: list[dict[str, Any]] = []
        for agent in self.agents:
            inputs = [message.agent_name for message in memory]
            output = agent.run(scenario, memory)
            memory.append(output)
            steps.append(
                {
                    "agent_name": output.agent_name,
                    "title": output.title,
                    "content": output.content,
                    "inputs": inputs,
                }
            )
        return steps


def format_block(message: AgentMessage) -> str:
    lines = [
        "=" * WRAP_WIDTH,
        f"{message.agent_name} | {message.title}",
        "-" * WRAP_WIDTH,
    ]
    for paragraph in message.content.split("\n"):
        if paragraph.strip().startswith("- ") or paragraph.strip().startswith("1."):
            lines.append(paragraph)
        elif paragraph.strip():
            lines.append(fill(paragraph, width=WRAP_WIDTH))
        else:
            lines.append("")
    return "\n".join(lines)


def format_intro(scenario: LessonScenario) -> str:
    intro = [
        "=" * WRAP_WIDTH,
        "DEMONSTRACJA: WSPOLPRACA AI-AGENTOW",
        "-" * WRAP_WIDTH,
        f"Temat: {scenario.title}",
        "",
        "Polecenie od uzytkownika:",
        fill(scenario.user_goal, width=WRAP_WIDTH),
        "",
        "Kontekst:",
        fill(scenario.context, width=WRAP_WIDTH),
    ]
    return "\n".join(intro)


def default_scenario() -> LessonScenario:
    return LessonScenario(
        title="Czy szkola powinna wdrozyc AI-asystenta?",
        user_goal=(
            "Przygotuj rekomendacje dla dyrekcji szkoly: czy warto wdrozyc "
            "AI-asystenta pomagajacego uczniom w nauce i nauczycielom w organizacji pracy?"
        ),
        context=(
            "System ma byc przydatny edukacyjnie, ale szkola musi brac pod uwage "
            "bezpieczenstwo, jakosc odpowiedzi, prywatnosc danych i ryzyko naduzyc."
        ),
    )


def scenario_to_dict(scenario: LessonScenario) -> dict[str, str]:
    return {
        "title": scenario.title,
        "user_goal": scenario.user_goal,
        "context": scenario.context,
    }


def print_conclusion(messages: list[AgentMessage]) -> None:
    print("=" * WRAP_WIDTH)
    print("PODSUMOWANIE DLA KLASY")
    print("-" * WRAP_WIDTH)
    print(
        fill(
            "Jeden chatbot moglby od razu dac odpowiedz, ale tutaj widzimy cos innego: "
            "zadanie zostalo rozlozone na role, a wynik koncowy powstal z wielu etapow pracy.",
            width=WRAP_WIDTH,
        )
    )
    print()
    print(
        fill(
            "To jest glowna idea systemow agentowych: specjalizacja, wspolpraca i przekazywanie "
            "wynikow pomiedzy agentami.",
            width=WRAP_WIDTH,
        )
    )
    print("=" * WRAP_WIDTH)


def main() -> None:
    scenario = default_scenario()
    demo = MultiAgentLessonDemo()
    messages = demo.run(scenario)

    print(format_intro(scenario))
    print()
    for message in messages:
        print(format_block(message))
        print()
    print_conclusion(messages)


if __name__ == "__main__":
    main()
