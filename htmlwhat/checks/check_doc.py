from protowhat.failure import InstructorError
from bs4.element import Doctype
from protowhat.Feedback import FeedbackComponent


def check_doctype(
        state, 
        missing_msg="Are you sure you defined `<{{tag}}>`?", 
        expand_msg="Did you correctly specify the `<{{tag}}>`?", 
        append=False, 
        **kwargs
    ):
    
    """
    Check whether the student code contain the :code:`<!DOCTYPE>` tag at the first line or not.

    It compares the first element or tag of the solution and student AST (Abstract Syntax Tree) of state to determine if the :code:`<!DOCTYPE>` tag is present.

    :param state: State instance describing student and solution code. Can be omitted if used with :code:`Ex()`.
    :type state: object

    :param missing_msg: Message to display if ``<!DOCTYPE>`` tag is missing in student code.
    :type missing_msg: str, optional

    :param expand_msg: If specified, this overrides any messages that are prepended by previous SCT chains.
    :type expand_msg: str, optional

    :param append: Whether to append the message into the message chain. Only work if this test failed, it does not break the chain if future test fails. Basically, only the message of this function will be provided on fail.
    :type append: bool, optional

    :param kwargs: By default :code:`missing_msg` and :code:`expand_msg` uses jinja template so you can provide additional information using :code:`kwargs` to add in feedback. default :code:`tag="!DOCTYPE"` is not modifiable.

    :return: The child State object with appropriate messages and ASTs.
    :rtype: State

    :raises InstructorError: If :code:`<!DOCTYPE>` tag is not found in solution code.
    :raises TestFail: If :code:`<!DOCTYPE>` tag is not found in student code. (aka feedback)

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import check_doctype
        >>> student_code = \"\"\" \"\"\"
        >>> solution_code = \"\"\"
        ... <!DOCTYPE html>
        ... <html>
        ...    <head>
        ...    </head>
        ...    <body>
        ...    </body>
        ... </html>
        ... \"\"\"
        >>> state = State(student_code=student_code, solution_code=solution_code)
        >>> check_doctype(state)
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Are you sure you defined `<!DOCTYPE>`?
    """

    kwargs["tag"] = "!DOCTYPE"

    expand_msg = FeedbackComponent(expand_msg, kwargs=kwargs)

    solution_ = state.solution_ast.contents[0] if state.solution_ast.contents else None
    student_ = state.student_ast.contents[0] if state.student_ast.contents else None

    if not isinstance(solution_, Doctype):
        raise InstructorError.from_message(
            "`check_doctype()` couldn't find `<!DOCTYPE>` tag in solution."
        )
    if not isinstance(student_, Doctype):
        state.report(missing_msg, append=append, kwargs=kwargs)

    return state.to_child(append_message=expand_msg, **{
        "solution_ast": solution_,
        "student_ast": student_
    })
