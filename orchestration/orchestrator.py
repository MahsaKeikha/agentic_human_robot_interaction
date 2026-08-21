from AGENTS.interaction_research_agent import InteractionResearchAgent
from AGENTS.ux_design_agent import UXDesignAgent
from AGENTS.accessibility_agent import AccessibilityAgent
from AGENTS.trust_calibration_agent import TrustCalibrationAgent
from AGENTS.safety_review_agent import SafetyReviewAgent
from AGENTS.evaluation_agent import EvaluationAgent
A=[InteractionResearchAgent(),UXDesignAgent(),AccessibilityAgent(),TrustCalibrationAgent(),SafetyReviewAgent(),EvaluationAgent()]
def run(c): return {"system":"F78","results":[a.run(c) for a in A],"physical_control":False}
