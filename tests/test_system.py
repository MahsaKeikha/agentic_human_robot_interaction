from orchestration.orchestrator import run
from safety.gate import authorize
def test_run(): assert run({"objective":"x"})["physical_control"] is False
def test_gate(): assert authorize("robot_command")["allowed"] is False
