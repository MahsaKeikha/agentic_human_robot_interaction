from orchestration.orchestrator import run


def base():
    return {
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "consent_missing": True}, False),
    ({**base(), "privacy_intrusion": True}, False),
    ({**base(), "accessibility_gap": True}, False),
    ({**base(), "trust_overreliance_risk": True}, False),
    ({**base(), "uncertainty_hidden": True}, False),
    ({**base(), "unsafe_proximity": True}, False),
    ({**base(), "manipulative_interaction": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
