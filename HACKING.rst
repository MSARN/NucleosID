NucleosID Style
===============

The NucleosID software is written in Python and adopt the same coding
style than the OpenStack project. To check the style of your code,
you must use **pep8** and **flake8** through *hacking*.

Concerning documentation written in ReStructuredText format (*.rst*),
the **doc8** tool should be used to verify the formatting.


hacking
-------

hacking is a set of flake8 plugins that test and enforce the OpenStack
StyleGuide.

Hacking pins its dependencies, as a new release of some dependency can
break hacking based gating jobs. This is because new versions of
dependencies can introduce new rules, or make existing rules stricter.

hacking is available from pypi, so just install it with:

.. code-block:: python

   pip install hacking

The canonical source of the OpenStack Style Guidelines is `StyleGuide <https://docs.openstack.org/hacking/latest/user/hacking.html#styleguide>`_,
and hacking just enforces them. So, please read this document to
write code that meets the project's expectations.
