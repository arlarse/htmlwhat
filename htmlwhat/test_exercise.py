from htmlwhat.State import State
from htmlwhat.sct_syntax import SCT_CTX
from htmlwhat.failure import TestFail


def test_exercise(
        sct: str,
        student_code: str,
        solution_code: str,
)-> dict:
    """
    Test an exercise with a student's code and a solution code directly.

    :param sct: The SCT (Submission Correctness Test) code to evaluate the student's code against.
    :type sct: str

    :param student_code: The code written by the student.
    :type student_code: str
    
    :param solution_code: The correct solution code.
    :type solution_code: str
    
    :return: Test result, a dictionary with the keys ``'correct'`` and ``'message'``.
    :rtype: dict

    :raises InstructorError: If anything wrong in the solution code.

    :example:
        >>> from htmlwhat import test_exercise
        >>> userhtml = \"\"\"
        ... <!DOCTYPE html>
        ... <html>
        ...     <head>
        ...         <title>Title</title>
        ...     </head>
        ...     <body class="hello">
        ...         <h1>My First Heading</h1>
        ...     </body>
        ... </html>
        ... \"\"\"
        >>> solutionhtml = \"\"\"
        ... <!DOCTYPE html>
        ... <html>
        ...     <head>
        ...         <title>Title</title>
        ...     </head>
        ...     <body class="example">
        ...         <h1>My First Heading</h1>
        ...     </body>
        ... </html>
        ... \"\"\"
        >>> test = "Ex().check_body().has_equal_attr()"
        >>> test_exercise(test, userhtml, solutionhtml)
        {
            'correct': False, 
            'message': 'Inspect the <code>&lt;body&gt;</code> tag. Expected attribute <code>class</code> to be <code>"example"</code>, but found <code>"hello"</code>.'
        }

        In case if the student's code is correct then the result will be:

        .. code-block:: python

            {'correct': True, 'message': 'Great work!'}

        This function automatically convert feedback into html.
    """

    state = State(student_code, solution_code)

    SCT_CTX["Ex"].root_state = state
    try:
        exec(sct, SCT_CTX)
    except TestFail as e:
        return state.reporter.build_failed_payload(e.feedback)

    return state.reporter.build_final_payload()
