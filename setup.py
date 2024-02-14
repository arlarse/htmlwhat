from setuptools import setup
from htmlwhat import __version__

PACKAGE_NAME = "htmlwhat"
DESCRIPTION = 'Verify HTML code submissions and auto-generate meaningful feedback messages.'

INSTALL_REQUIRES = [
    'beautifulsoup4~=4.12.3',
    'protowhat~=2.1.3'
]

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=PACKAGE_NAME,
    version=__version__,
    author="SHRAY SALVI",
    author_email="shraysalvi@yahoo.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=[PACKAGE_NAME, "htmlwhat.checks"],
    install_requires=INSTALL_REQUIRES,
    keywords=['htmlwhat', 'html', 'feedback', 'html validation', "testing", "html testing"],
    url="https://github.com/arlarse/htmlwhat",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
