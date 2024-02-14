from htmlwhat.State import State
from htmlwhat.sct_syntax import SCT_CTX
from htmlwhat.failure import InstructorError, TestFail


def test_exercise(
        sct: str,
        student_code: str,
        solution_code: str,
):
    """
        Test an exercise with a student's code and a solution code directly.
    """

    state = State(student_code, solution_code)

    SCT_CTX["Ex"].root_state = state
    try:
        exec(sct, SCT_CTX)
    except TestFail as e:
        return state.reporter.build_failed_payload(e.feedback)

    return state.reporter.build_final_payload()
