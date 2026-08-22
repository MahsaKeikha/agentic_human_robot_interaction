from AGENTS.accessibility_agent import AccessibilityAgent
from AGENTS.evaluation_agent import EvaluationAgent
from AGENTS.interaction_research_agent import InteractionResearchAgent
from AGENTS.safety_review_agent import SafetyReviewAgent
from AGENTS.trust_calibration_agent import TrustCalibrationAgent
from AGENTS.ux_design_agent import UXDesignAgent
from safety.gate import authorize

AGENTS = [
    InteractionResearchAgent(),
    UXDesignAgent(),
    AccessibilityAgent(),
    TrustCalibrationAgent(),
    SafetyReviewAgent(),
    EvaluationAgent(),
]


def run(context: dict) -> dict:
    """Run six HRI specialists and apply the fail-closed release gate."""
    results = [agent.run(context) for agent in AGENTS]
    governance = authorize("analysis_release", context)
    return {
        "system": "F78",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "physical_control": False,
        "autonomous_physical_contact": False,
        "coercive_interaction": False,
    }
