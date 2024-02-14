from protowhat.failure import InstructorError
from bs4.element import Tag
from htmlwhat.utils import number_to_position, check_str
from protowhat.Feedback import FeedbackComponent


EXPND_MSG = "Inspect the `<{{tag}}>` tag"
MISSING_MSG = "Are you sure you included `<{{tag}}>` tag?"


def check_html(state, missing_msg=MISSING_MSG, expand_msg=EXPND_MSG, append=False, **kwargs):
    """
    Check whether the student code contain the ``<html>`` tag or not.

    :param state: State instance describing student and solution code. Can be omitted if used with :code:`Ex()`.
    :type state: object
    
    :param missing_msg: Message to display if ``<html>`` tag is missing in student code.
    :type missing_msg: str, optional
    
    :param expand_msg: If specified, this overrides any messages that are prepended by previous SCT chains.
    :type expand_msg: str, optional

    :param append: Whether to append the message into the message chain. Only work if this test failed, it does not break the chain if future test fails. Basically, only the feedback of this function will be provided on fail.
    :type append: bool, optional

    :param kwargs: Additional keyword arguments to pass into ``missing_msg`` or ``expand_msg`` jinja template.

    :return: The child State object with appropriate messages and ASTs.
    :rtype: State

    :raises InstructorError: If ``<html>`` tag is not found in solution code.
    :raises TestFail: If ``<html>`` tag is not found in student code. (aka feedback)

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import check_html
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
        >>> check_html(state)
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Are you sure you included `<html>` tag?
    """

    kwargs["tag"] = "html"

    expand_msg = FeedbackComponent(expand_msg, kwargs=kwargs)

    if not isinstance(state.solution_ast.html, Tag):
        raise InstructorError.from_message(
            "`check_html()` couldn't find `<html>` tag in solution"
        )

    if not isinstance(state.student_ast.html, Tag):
        state.report(missing_msg, append=append, kwargs=kwargs)

    return state.to_child(append_message=expand_msg, **{
        "solution_ast": state.solution_ast.html,
        "student_ast": state.student_ast.html
    })


def check_head(state, missing_msg=MISSING_MSG, expand_msg=EXPND_MSG, append=False, **kwargs):
    """
    Check whether the student code contains the ``<head>`` tag or not.

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object
    
    :param missing_msg: Message to display if ``<head>`` tag is missing in student code.
    :type missing_msg: str, optional
    
    :param expand_msg: If specified, this overrides any messages that are prepended by previous SCT chains.
    :type expand_msg: str, optional

    :param append: Whether to append the message into the message chain. Only work if this test failed, it does not break the chain if future test fails. Basically, only the feedback of this function will be provided on fail.
    :type append: bool, optional

    :param kwargs: Additional keyword arguments to pass into ``missing_msg`` or ``expand_msg`` jinja template.

    :return: The child State object with appropriate messages and ASTs.
    :rtype: State

    :raises InstructorError: If ``<head>`` tag is not found in solution code.
    :raises TestFail: If ``<head>`` tag is not found in student code.

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import check_head
        >>> student_code = \"\"\"\"\"\"
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
        >>> check_head(state)
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Are you sure you included `<head>` tag?
    """

    kwargs["tag"] = "head"

    expand_msg = FeedbackComponent(expand_msg, kwargs=kwargs)

    if not isinstance(state.solution_ast.head, Tag):
        raise InstructorError.from_message(
            f"`check_head()` couldn't find `<head>` tag in `<{state.solution_ast.name}>`"
        )

    if not isinstance(state.student_ast.head, Tag):
        state.report(missing_msg, append=append, kwargs=kwargs)

    return state.to_child(append_message=expand_msg, **{
        "solution_ast": state.solution_ast.head,
        "student_ast": state.student_ast.head
    })


def check_body(state, missing_msg=MISSING_MSG, expand_msg=EXPND_MSG, append=False, **kwargs):
    """
    Check whether the student code contains the ``<body>`` tag or not.

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object
    
    :param missing_msg: Message to display if ``<body>`` tag is missing in student code.
    :type missing_msg: str, optional
    
    :param expand_msg: If specified, this overrides any messages that are prepended by previous SCT chains.
    :type expand_msg: str, optional

    :param append: Whether to append the message into the message chain. Only work if this test failed, it does not break the chain if future test fails. Basically, only the feedback of this function will be provided on fail.
    :type append: bool, optional

    :param kwargs: Additional keyword arguments to pass into ``missing_msg`` or ``expand_msg`` jinja template.

    :return: The child State object with appropriate messages and ASTs.
    :rtype: State

    :raises InstructorError: If ``<body>`` tag is not found in solution code.
    :raises TestFail: If ``<body>`` tag is not found in student code.

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import check_body
        >>> student_code = \"\"\"\"\"\"
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
        >>> check_body(state)
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Are you sure you included `<body>` tag?
    """

    kwargs["tag"] = "body"

    expand_msg = FeedbackComponent(expand_msg, kwargs=kwargs)

    if not isinstance(state.solution_ast.body, Tag):
        raise InstructorError.from_message(
            f"`check_body()` couldn't find `<body>` tag in `<{state.solution_ast.name}>`"
        )

    if not isinstance(state.student_ast.body, Tag):
        state.report(missing_msg, append=append, kwargs=kwargs)

    return state.to_child(append_message=expand_msg, **{
        "solution_ast": state.solution_ast.body,
        "student_ast": state.student_ast.body
    })


def check_tag(
        state, 
        name: str, 
        index=0, 
        missing_msg="Did you include the {{index}}`{{tag}}` tag properly?", 
        expand_msg="Check the {{index}}`{{tag}}` tag", 
        append=True, 
        **kwargs
    ):
    """
    Check the presence of a specific tag in the student code. This is a generic function that can be used to 
    check for any tag, **it will only check the direct children of the current state or tag**.

    .. code-block:: html
    
        <body>
            <div> <!-- 1st -->
                <div> <!-- 2st -->
                </div>
            </div>
            <div> <!-- 3rd -->
            </div>
        </body>

    In the code above div 1st and 3rd are direct children of body tag, and div 2nd is a direct child of div 1st.

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object

    :param name: The name of the tag to check for. If you want to check for ``<span>`` tag then pass ``"span"``.
    :type name: str

    :param index: The index of the tag to check for. If there are multiple tags with the same name, you can specify the index (0-based indexing) to check for. Default is 0.
    :type index: int, optional

    :param missing_msg: Message to display if given tag is missing in student code.
    :type missing_msg: str, optional

    :param expand_msg: If specified, this overrides any messages that are prepended by previous SCT chains.
    :type expand_msg: str, optional

    :param append: Whether to append the message into the message chain. Only work if this test failed, it does not break the chain if future test fails. Basically, only the feedback of this function will be provided on fail.
    :type append: bool, optional

    :param kwargs: Additional keyword arguments to pass into ``missing_msg`` or ``expand_msg`` jinja template.

    :return: The child State object with appropriate messages and ASTs.
    :rtype: State

    :raises InstructorError: If the given tag is not found in solution code.
    :raises TestFail: If the given tag is not found in student code.

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import check_tag, check_body, check_html
        >>> student_code = \"\"\"
        ... <!DOCTYPE html>
        ... <html>
        ...    <body>
        ...    </body>
        ... </html>
        ... \"\"\"
        >>> solution_code = \"\"\"
        ... <!DOCTYPE html>
        ... <html>
        ...    <head>
        ...    </head>
        ...    <body>
        ...        <div>
        ...        </div>
        ...    </body>
        ... </html>
        ... \"\"\"
        >>> state = State(student_code=student_code, solution_code=solution_code)
        >>> html_state = check_html(state)  # 1st test
        >>> body_state = check_body(html_state)  # 2nd test
        >>> check_tag(body_state, "div")  # 3rd test
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Inspect the `<body>` tag with in `html`. Did you include the `div` tag properly?
    """

    tag = name.lower() if check_str(name, _for="arg: name") else None

    solution_tags = state.solution_ast.find_all(tag, recursive=False)
    student_tags = state.student_ast.find_all(tag, recursive=False)

    if len(solution_tags) <= index:
        raise InstructorError.from_message(
            f"`check_tag()` couldn't find `<{tag}>` tag in `<{state.solution_ast.name}>` at index {index}"
        )

    kwargs.update({
        "tag": tag,
        "index": (number_to_position(index+1)+" ") if len(solution_tags) > 1 else ""
    })

    if len(student_tags) <= index:
        state.report(missing_msg, append=append, kwargs=kwargs)

    expand_msg = FeedbackComponent(expand_msg, kwargs=kwargs)

    return state.to_child(append_message=expand_msg, **{
        "solution_ast": solution_tags[index],
        "student_ast": student_tags[index]
    })


# TODO: create check_path, check_css_pattern, remaining
