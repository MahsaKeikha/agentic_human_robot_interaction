from orchestration.orchestrator import run

context = {
    "objective": "review a simulated HRI study",
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

print(run(context))
