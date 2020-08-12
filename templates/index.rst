.. ose-code-templates documentation master file, created by
   sphinx-quickstart on Tue May 19 21:22:18 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ose-code-templates
===================

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