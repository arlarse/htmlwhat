# htmlwhat

`htmlwhat` is a Python module that provides feedback on incorrect HTML code submissions. It's often used in educational platforms where students submit HTML code as part of their assignments or exercises.

## Installation

```
# latest stable version from PyPi
pip install htmlwhat

# latest development version from GitHub
pip install git+https://github.com/arlarse/htmlwhat
```

## Quick Start
```python
from htmlwhat.test_exercise import test_exercise

userhtml = """
<!DOCTYPE html>
<html>
    <head>
        <title>Title</title>
    </head>
    <body class="hello">
        <h1>My First Heading</h1>
    </body>
</html>
"""

solutionhtml = """
<!DOCTYPE html>
<html>
    <head>
        <title>Title</title>
    </head>
    <body class="example">
        <h1>My First Heading</h1>
    </body>
</html>
"""

test = "Ex().check_body().has_equal_attr()"

print(test_exercise(
    test,
    userhtml,
    solutionhtml,
))
```
Output:
```json
{'correct': False, 'message': 'Inspect the <code>&lt;body&gt;</code> tag. Expected attribute <code>class</code> to be <code>"example"</code>, but found <code>"hello"</code>.'}
```

## Problems after installation

htmlwhat built over ``protowhat`` which uses ``jinja2==2.11.3``, and jinja uses ``MarkupSafe==2.0.1``.
Hence you will face this error

```
ImportError: cannot import name 'soft_unicode' from 'markupsafe'
```

so install the latest version of jinja2 using the following command:

```
pip install --upgrade jinja2
```
