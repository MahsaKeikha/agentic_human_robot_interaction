from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "human robot interaction review",
    "interaction_research_reviewed": True,
    "ux_reviewed": True,
    "accessibility_reviewed": True,
    "trust_calibration_reviewed": True,
    "consent_reviewed": True,
    "privacy_reviewed": True,
    "uncertainty_disclosure_reviewed": True,
    "proximity_safety_reviewed": True,
    "evaluation_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
