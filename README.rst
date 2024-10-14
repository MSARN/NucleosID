==========
Nucleos'ID
==========

|doi| |license| |OpenSSF Best Practices|

.. |OpenSSF Best Practices| image:: https://www.bestpractices.dev/projects/9547/badge
   :target: https://www.bestpractices.dev/projects/9547

:Version: 1.0.0
:Download: https://github.com/MSARN/NucleosID/releases
:Source: https://github.com/MSARN/NucleosID
:Keywords: scientific software, RNA, mass spectrometry, nucleoside,
    python

Nucleos'ID is a Python-based software to identify post-transcriptional modifications
of RNA at the nucleoside level.

.. image:: https://github.com/MSARN/NucleosID/raw/main/nucleosid/images/nucleosid-logo.png 
   :align: center

Installation
============

Binaries
--------

Binaries for Windows are available on the `release page
<https://github.com/MSARN/NucleosID/releases>`_.


From source
-----------

Prerequisites
+++++++++++++

If you are installing from source, you will need:

* `Python 3 <https://www.python.org/>`_

* A `git <https://git-scm.com/>`_ client

To get the source, clone the last version of Nucleos'ID repository:

.. code-block::

   git clone https://github.com/MSARN/NucleosID.git

Install the software
++++++++++++++++++++

First, install the dependencies:

.. code-block:: 

   pip3 install -r requirements.txt

Then, build and install the software:

.. code-block::

   python3 setup.py install


Bug tracker
===========

If you have any suggestions, bug reports, or annoyances please report
them to our issue tracker at https://github.com/MSARN/NucleosID/issues.

Citation
========

As part of the research process, it is important that pieces of software
that have contributed to the research are cited. You can cite Nucleos'ID
with the following text:

The Nucleos'ID software has been used to identify post-transcriptional
modifications. The source code is available on GitHub[1] and archived in Zenodo[2].

#. https://github.com/MSARN/NucleosID

#. Didierjean, M., Gosset-Erard, C. François, Y. & Pansanel, J. Nucleos'ID v1.0.0.
   *Zenodo* **2022**, https://doi.org/10.5281/zenodo.7223373


License
=======

Nucleos'ID is released under the Apache 2.0 license, as found
in the `LICENSE <LICENSE>`_ file.

.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.7223373.svg
   :target: https://doi.org/10.5281/zenodo.7223373

.. |license| image:: https://img.shields.io/badge/License-Apache_2.0-blue.svg
    :alt: Apache 2.0 
    :target: https://opensource.org/licenses/Apache-2.0
