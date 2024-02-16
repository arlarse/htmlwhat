Check Multiple Tags
===================

Until this point, we were checking straightforward HTML tags, but what if we want to check for multiple tags? 
For example, you might want to check for all the ``li`` tags inside ``ol`` tag. This involves a more complex check,
as it requires us to examine the hierarchical structure of the HTML code.

And we have ``multi()`` for that. This function is used to **branch different chains** of test functions, 
so that the same state is passed to all sub-chains. Most commonly, ``multi()`` is used to convert this code

.. code:: python

    Ex().check_body().check_tag("ol").check_tag("li", 0)
    Ex().check_body().check_tag("ol").check_tag("li", 1)
    Ex().check_body().check_tag("ol").check_tag("li", 2)
    Ex().check_body().check_tag("ol").check_tag("li", 3)
    Ex().check_body().check_tag("ol").check_tag("li", 4)
    Ex().check_body().check_tag("ol").check_tag("li", 5)


into this equivalent (and more performant) SCT:

.. code:: python

    Ex().check_body().check_tag("ol").multi(
        check_tag("li", 0),
        check_tag("li", 1),
        check_tag("li", 2),
        check_tag("li", 3),
        check_tag("li", 4),
        check_tag("li", 5),
    )

Still the syntax is quite long but we can use ``for`` loop to make it shorter.

.. code:: python

    Ex().check_body().check_tag("ol").multi(
        check_tag("li", index) for index in range(6)
    )

Hence, all the above code check for all the ``li`` tags inside ``ol`` but the last one is the most efficient way to do it.

.. function:: multi(state, *tests)

    Run multiple subtests. This function could be thought as an AND statement, since all tests it runs must pass

    :param state: State instance describing student and solution code. Can be omitted if used with :code:`Ex()`.
    :type state: object

    :param tests: One or more SCT/test functions to be branched.

    :return: The similar State object.
    :rtype: State

    :example:

        >>> Ex().check_body().check_tag("h1").multi(
        ...    has_equal_attr(),
        ...    has_equal_text()
        ... )

        The above SCT checks if the first ``h1`` tag has the same attributes and text as the solution code.

        >>> Ex().check_body().check_tag("form").multi(
        ...    check_tag("input", index).has_equal_attr("name") for index in range(3)
        ... )

        The above SCT checks if the first three ``input`` tags inside the first ``form`` tag have the same ``name`` attribute as the solution code.

.. note::

    The ``multi()`` function returns the same state, it was given. So whatever comes after multi will run the same as if multi wasn't used.

.. caution::
    
    Bad practice

    .. code:: python

        Ex().check_body().check_tag("ol").multi(
            check_tag("li", 0),
        ).has_equal_attr()

    Good practice, first complete all check's of a tag and then move to the next tag.

    .. code:: python

        Ex().check_body().check_tag("ol").multi(
            has_equal_attr(),
            check_tag("li", 0),
        )

.. function:: check_not(state, *tests, msg)
    
    This function can be considered a direct counterpart of multi. It run multiple subtests that should
    fail. If all subtests fail, returns original state (for chaining)

    - This function is currently only tested in working with ``has_code()`` in the subtests.
    - This function can be thought as a ``NOT(x OR y OR ...)`` statement, since all tests it runs must fail.

    :param state: State instance describing student and solution code. Can be omitted if used with :code:`Ex()`.
    :type state: object

    :param tests: One or more sub-SCTs/test functions to run.

    :param msg: Feedback message that is shown in case not all tests specified in ``*tests`` fail.
    :type msg: str

    :return: The original State object.
    :rtype: State

    :Example:

        The SCT below runs two has_code cases. ::

            Ex(state).check_body().check_tag("form").check_not(
                has_code('style=".*?"', fixed=False),
                has_code('height=".*?"', fixed=False),
                msg="Don't use inline styles with form"
            )

        If students use ``style="any style"`` or ``height="any value"`` in their code, this test will fail.

.. function:: check_or(state, *tests)
    
    Check whether at least one SCT is correct.

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object

    :param tests: One or more sub-SCTs/test functions to run.

    :Example:
        The SCT below tests that the student tag has ``class`` attribute or ``data-class`` attribute. ::

            Ex(state).check_body().check_or(
                has_code('class=".*?"', fixed=False),
                has_code('data-class=".*?"', fixed=False),
            )

.. function:: check_correct(state, check, diagnose)

    Allows feedback from a diagnostic SCT, only if a check SCT fails.

    :param state: State instance describing student and solution code. Can be omitted if used with ``Ex()``.
    :type state: object

    :param check: An sct chain that must succeed.
    
    :param diagnose: An sct chain to run if the check fails.

    :Example:
        The SCT below tests whether ``head`` tag has code ``Welcome`` in it before diagnose SCT. ::

            Ex().check_head().check_correct(
                has_code("Welcome"),
                check_tag("title").has_equal_text()
            )