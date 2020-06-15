==================
OSE code templates
==================

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


|

We maintain a set of code templates on selected issues. They help in the onboarding of new
contributors and also serve as a teaching resource. If you have any questions or suggestions,
please do not hesitate to contact us on `Zulip <https://OpenSourceEconomics.zulipchat.com>`_

Material
========

We have just started with the templates, so our current offer is rather limited.

`Parallelize an embarrassingly parallel loop <https://github.com/OpenSourceEconomics/ose-code-templates/blob/master/templates/01_embarssingly_parallel_loop/run.py>`_
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

We show how to parallelize a loop using the ``multiprocessing`` and ``mpi4py``. The setup allows to
seamlessly switch between shared and distributed memory computing.

`Parallelization with numba <https://github.com/OpenSourceEconomics/ose-code-templates/blob/master/templates/02_numba_parallel/02_numba_parallel.ipynb>`_
---------------------------------------------------------------------------------------------------------------------------------------------------------

We collect resources and demonstrate parallelization with numba. Our focus lies on the
analysis of nested parallelism. The working example is inspired by `respy`.
