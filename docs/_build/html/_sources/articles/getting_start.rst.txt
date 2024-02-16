Getting Start with htmlwhat
=============================

``htmlwhat`` works by comparing the user's HTML code with a solution code using an abstract syntax tree (AST). 
The AST represents the structure of the HTML code and allows for easy comparison and analysis. 
The module is inspired by the datacamp's `pythonwhat` module and is built on top of `beautifulsoup` and `protowhat`.

When a test is run, the AST of the student's HTML code is generated and compared with the AST of the solution HTML code. 
If there are any differences or mismatches, the module generates meaningful feedback to guide the student in the right direction.

Overall, ``htmlwhat`` is a powerful tool for verifying HTML code submissions and providing targeted feedback to help students learn and improve their coding skills.

Example 1
--------------

Here's an HTML sample code for student and solution that I'll be using as an example

.. code-block:: python

    solution_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Web Page</title>
    </head>
    <body class="example">
        <h1>Welcome to My Web Page</h1>
        <p>This is a sample HTML code.</p>
    </body>
    </html>
    """

    student_code = """"""

Now Let's verify if the student/user code contains HTML tags or not.

.. code-block:: python

    from htmlwhat.State import State
    from htmlwhat.checks import check_body

    # Initialize a state object to maintain the student code and solution code 
    # together during the test.
    state = State(student_code, solution_code)

    # Verifying if the student code contains body tag.
    check_body(state)

When you run the above code, you will get the following output:

.. code-block:: bash

    Traceback (most recent call last):
    protowhat.failure.TestFail: Are you sure you included `<body>` tag?

The output indicates that the student's body code is missing the ``<body>`` tag, and 
the feedback provides a hint to help the student fix the issue.

Example 2
--------------

Now let's modify the student code and include the ``<body>`` tag, 

.. code-block:: python

    student_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Web Page</title>
    </head>
    <body class="hello">
        <h1>Welcome to My Web Page</h1>
        <p>This is a sample HTML code.</p>
    </body>
    </html>
    """

but this time we will check if the student's ``body`` contains same class as solution i.e., ``"example"``.

.. code-block:: python

    from htmlwhat.State import State
    from htmlwhat.checks import check_body, has_equal_attr

    # Initialize a state object to maintain the student code and solution code 
    # together during the test.
    state = State(student_code, solution_code)

    # Verifying if the student code contains body tag.
    body_checked = check_body(state)

    # Verifying if the student's body tag has same class as solution.
    has_equal_attr(body_checked)

When you run the above code, you will get the following ``Traceback``:

.. code-block:: bash

    Inspect the `<body>` tag. Expected attribute `class` to be `"example"`, but found `"hello"`.

Installation
=============================

1. Install htmlwhat using ``pip`` by running the following command:

.. code-block:: bash

    pip install htmlwhat

or

2. Install from git repository using the following command:

.. code-block:: bash

    pip install git+https://github.com/arlarse/htmlwhat

Problems after installation
---------------------------

.. caution::

    htmlwhat built over ``protowhat`` which uses ``jinja2==2.11.3``, and jinja uses ``MarkupSafe==2.0.1``. 
    Hence you will face this error

.. code-block:: bash

    ImportError: cannot import name 'soft_unicode' from 'markupsafe'

so install the latest version of jinja2 using the following command:

.. code-block:: bash

    pip install --upgrade jinja2


