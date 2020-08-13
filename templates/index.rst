.. ose-code-templates documentation master file, created by
   sphinx-quickstart on Tue May 19 21:22:18 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. |logo| image:: https://raw.githubusercontent.com/OpenSourceEconomics/ose-corporate-design/master/logos/OSE_logo_no_type_RGB.svg
  :width: 4 %

|logo| OSE code templates
==========================


.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://opensource.org/licenses/MIT

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black

.. image:: https://github.com/openSourceEconomics/ose-code-templates/workflows/CI/badge.svg
    :target: https://github.com/OpenSourceEconomics/ose-code-templates/actions?query=workflow%3ACI

.. image:: https://codecov.io/gh/OpenSourceEconomics/ose-code-templates/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/OpenSourceEconomics/ose-code-templates

.. image:: https://img.shields.io/badge/zulip-join_chat-brightgreen.svg
    :target: https://OpenSourceEconomics.zulipchat.com

.. image:: https://readthedocs.org/projects/ose-code-templates/badge/?version=latest
    :target: https://ose-code-templates.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 1

   01_embarssingly_parallel_loop/index

We show how to parallelize a loop using the ``multiprocessing`` and ``mpi4py``. The setup allows
to seamlessly switch between shared and distributed memory computing.

.. toctree::
   :maxdepth: 1

   02_numba_parallel/02_numba_parallel.ipynb

We collect resources and demonstrate parallelization with ``numba``. Our focus lies on the
analysis of nested parallelism and the working example is inspired by ``respy``.

.. toctree::
   :maxdepth: 1

   03_mpi_main_child/index

We show how to set up a main-child application. We use the example of uncertainty propagation
using ``respy`` as the motivating use-case.

==========
Powered by
==========

.. image:: https://raw.githubusercontent.com/OpenSourceEconomics/ose-corporate-design/master/logos/OSE_logo_RGB.svg
  :width: 22 %
  :target: https://open-econ.org

