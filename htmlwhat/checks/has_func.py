from typing import Union, List, Tuple
from protowhat.failure import InstructorError
import re


def has_code(
    state,
    text: str,
    incorrect_msg: str = "Didn't find {{text}} in your code.",
    fixed: bool = True,
    append=True,
    **kwargs
):
    """
    Check whether the student code contains a specific text or follows a regex pattern. 
    This function is a primary designed for regex pattern matching and is solution and AST independent, 
    hence not required solution to contain the ``text``.

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object

    :param text: The text or regex pattern to search for in the student code.
    :type text: str

    :param incorrect_msg: The message to display if the text or pattern is not found in student code.
    :type incorrect_msg: str, optional

    :param fixed: Fixed should be ``False`` for regex ``text``. Default is True, for checking fixed text present in the student code.
    :type fixed: bool, optional

    :param append: Whether to append the message to the existing report. If ``False``, only the message of this function will display.
    :type append: bool, optional

    :param kwargs: Additional keyword arguments to pass into ``missing_msg`` or ``expand_msg`` jinja template.

    :return: The same State object with updatted messages. And hence recommended to use at the end of the chain.
    :rtype: State

    :raises TestFail: If the given ``text`` is not found in student code.  (aka feedback)

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import has_code
        >>> student_code = \"\"\"
        ... <!DOCTYPE html>
        ... <html>
        ...    <head>
        ...        <title>12-52-2524</title>
        ...    </head>
        ... </html>
        ... \"\"\"
        >>> solution_code = \"\"\" \"\"\"
        >>> state = State(student_code=student_code, solution_code=solution_code)
        >>> has_code(state, text=".*\d{3}-\d{2}-\d{4}.*", fixed=False)
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Didn't find the pattern `.*\d{3}-\d{2}-\d{4}.*` in your code.
    """
    student_code = state.student_ast.decode()
    res = text in student_code if fixed else re.search(text, student_code)

    kwargs["text"] = f"`{text}`" if fixed else f"the pattern `{text}`"

    if not res:
        state.report(incorrect_msg, append=append, kwargs=kwargs)
    return state


def has_equal_text(
    state,
    incorrect_msg: str = "Expected text not found.",
    show_text: bool = False,
    append: bool = True,
    **kwargs
):
    """
    Check whether the student and solution code have identical text. Keep in mind that this function get text of child tags as well.

    Hence in the code ``<body>Hello<p>this is paragraph</p>World</body>``, text of body is "Hello this is paragraph World" and not 
    only "Hello World".

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object

    :param incorrect_msg: The message to display if student text not equal to solution text.
    :type incorrect_msg: str, optional

    :param show_text: Whether to include the actual text in the error message. Default is False.
    :type show_text: bool, optional

    :param append: Whether to append the message to the existing report. If ``False``, only the message of this function will display.
    :type append: bool, optional

    :param kwargs: Additional keyword arguments to pass into ``missing_msg`` or ``expand_msg`` jinja template.

    :return: The same State object with updatted messages. And hence recommended to use at the end of the chain.
    :rtype: State

    :raises TestFail: If the student text is not strictly equal to the solution text.  (aka feedback)

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import check_head, check_tag, has_equal_text
        >>> student_code = \"\"\"
        ... <!DOCTYPE html>
        ...    <html>
        ...        <head>
        ...        <title>412-52-2524</title>
        ...        </head>
        ...    </html> 
        ... \"\"\"
        >>> solution_code = \"\"\"
        ... <!DOCTYPE html>
        ...    <html>
        ...        <head>
        ...        <title>412-52-2222</title>
        ...        </head>
        ...    </html> 
        ... \"\"\"
        >>> state = State(student_code=student_code, solution_code=solution_code)
        >>> head_state = check_head(state)
        >>> title_state = check_tag(head_state, "title")
        >>> has_equal_text(title_state, show_text=True)
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Check the `title` tag with in `head`. Expected text `412-52-2222` but found `412-52-2524`
    """
    kwargs["stu"] = student_text = state.student_ast.get_text(separator=" ", strip=True)
    kwargs["sol"] = solution_text = state.solution_ast.get_text(separator=" ", strip=True)

    if student_text != solution_text:
        state.report(
            "Expected text `{{sol}}` but found `{{stu}}`." if show_text else incorrect_msg,
            append=append, kwargs=kwargs
        )

    return state


def has_equal_attr(
    state,
    attrs: Union[List[str], Tuple[str]] = None,
    missing_msg: str = "Expected attribute `{{attr}}` not found.",
    incorrect_msg: str = 'Expected attribute `{{attr}}` to be `"{{sol}}"`, but found `"{{stu}}"`.',
    check_values: bool = True,
    append: bool = True,
    **kwargs
):
    """
    Check whether the student code have the same attributes as the solution code.

    This function first checks for the presence of attributes in the student code, 
    and if found then compares their values with the solution code.

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object

    :param attrs: The list or tuple of attributes of the solution to check. If ``None``, all attributes in the solution code will be checked.
    :type attrs: List[str] | Tuple[str] | None, optional

    :param missing_msg: Message to display if any attribute is missing in student code.
    :type missing_msg: str, optional

    :param incorrect_msg: Message to display if any attribute with the incorret value is found.
    :type incorrect_msg: str, optional

    :param check_values: Whether to check the attribute values for equality. If ``False``, only the presence of attributes will be checked.
    :type check_values: bool, optional

    :param append: Whether to append the message to the existing report. If ``False``, only the message of this function will display.
    :type append: bool, optional

    :param kwargs: Additional keyword arguments to pass into ``missing_msg`` or ``incorrect_msg`` jinja template.

    :return: The same State object with updatted messages. And hence recommended to use at the end of the chain.
    :rtype: State

    :raises InstructorError: If an attribute specified in ``attrs`` is missing in the solution code.
    :raises TestFail: If an attribute specified in ``attrs`` is missing in the student code or has an incorrect value. (aka feedback)

    :example:
        >>> from htmlwhat.State import State
        >>> from htmlwhat.checks import check_body, has_equal_attr
        >>> student_code = \"\"\"
        ... <!DOCTYPE html>
        ...    <html>
        ...        <head>
        ...        </head>
        ...        <body>
        ...        </body>
        ...    </html> 
        ... \"\"\"
        >>> solution_code = \"\"\"
        ... <!DOCTYPE html>
        ...    <html>
        ...        <head>
        ...        </head>
        ...        <body width="40px" class="example" >
        ...        </body>
        ...    </html> 
        ... \"\"\"
        >>> state = State(student_code=student_code, solution_code=solution_code)
        >>> body_state = check_body(state)
        >>> has_equal_attr(body_state)
        Traceback (most recent call last): ...
        protowhat.failure.TestFail: Inspect the `<body>` tag. Expected attribute `width` not found.

        Let's modify ``student_code``-

        >>> student_code = \"\"\"
        ... <!DOCTYPE html>
        ...    <html>
        ...        <head>
        ...        </head>
        ...        <body width="40px" class="hello">
        ...        </body>
        ...    </html> 
        ... \"\"\"

        And run the code again,

        .. code-block:: bash
        
            Inspect the `<body>` tag. Expected attribute `class` to be `"example"`, but found `"hello"`.

    """

    if attrs is not None and not isinstance(attrs, (list, tuple)):
        raise TypeError("attrs should be a list, tuple or None.")
    elif attrs is None:
        attrs = state.solution_ast.attrs.keys()
    else:
        sol_attrs = state.solution_ast.attrs.keys()
        for _ in attrs:
            if _ not in sol_attrs:
                raise InstructorError.from_message(
                    f"`has_equal_attr()` couldn't find attribute `{_}` in `<{state.solution_ast.name}>`."
                )

    for attr in attrs:
        stu_attr_val = state.student_ast.get(attr)
        sol_attr_val = state.solution_ast.get(attr)

        if stu_attr_val is None:
            # for not found attributes
            kwargs["attr"] = attr
            state.report(missing_msg, append=append, kwargs=kwargs)

        elif check_values and stu_attr_val != sol_attr_val:
            # for incorrect attribute values
            sol_attr_is_list = isinstance(sol_attr_val, list)
            if sol_attr_is_list and set(stu_attr_val) == set(sol_attr_val):
                continue
            kwargs["attr"] = attr
            kwargs["sol"] = " ".join(sol_attr_val) if sol_attr_is_list else sol_attr_val
            kwargs["stu"] = " ".join(stu_attr_val) if sol_attr_is_list else stu_attr_val
            state.report(incorrect_msg, append=append, kwargs=kwargs)

    return state

# TODO: create has_equal_js, has_equal_style, remaining 
