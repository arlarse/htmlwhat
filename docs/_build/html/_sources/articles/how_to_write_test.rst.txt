.. _How to Write Tests:

How to Write Tests
==================

In the previous section, we discussed some basic tests.
However, it is important to note that this approach may not always be ideal or satisfying.

To streamline your testing process and enhance efficiency, we have developed a method known as 
'functional chaining'. This approach allows you to link multiple test functions together in a single, 
cohesive operation.

htmlwhat uses the ``.`` to "chain together" SCT/test functions. Every chain starts with the ``Ex()`` 
function call, which holds exercise state. Hence it automatically take cares about ``State``. 
Let's have a look on it.

.. autofunction:: htmlwhat.test_exercise

.. tip::
    - You can use ``from htmlwhat.failure import InstructorError, TestFail`` to handle exceptions.
    - Also, you can use ``to_html`` function of the ``from htmlwhat.Reporter import Reporter`` to convert your test report into html.

    .. code-block:: python

        from htmlwhat.Reporter import Reporter
        from htmlwhat.failure import InstructorError, TestFail
        from htmlwhat import test_exercise
        try:
            test_exercise()
        except InstructorError as e:
            Reporter.to_html(str(e))

