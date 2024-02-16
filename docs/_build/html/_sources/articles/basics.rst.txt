Check Tags
==============

``htmlwhat.check`` contain all the check related functions. ``check_`` functions are 
responsible for verifying the presence of HTML tags in a given code.

.. autofunction:: htmlwhat.checks.check_doctype

.. note:: 

    - If you are not familiar with what ``Ex()`` is at the moment, don't worry. It will be explained in the :ref:`How to Write Tests` section.

.. autofunction:: htmlwhat.checks.check_html
.. autofunction:: htmlwhat.checks.check_head
.. autofunction:: htmlwhat.checks.check_body
.. autofunction:: htmlwhat.checks.check_tag


Check Tag Values 
====================

Now we know how to check a tag present in the code. But what if we want to check the values or attributes of a tag?
``has_`` functions are responsible for verifying the presence of different kind of values in a given tag. 
This functions always return the state that they were intially passed and are recommended to use at the 'end' of a chain.

.. autofunction:: htmlwhat.checks.has_equal_attr
.. autofunction:: htmlwhat.checks.has_equal_text
.. autofunction:: htmlwhat.checks.has_code
