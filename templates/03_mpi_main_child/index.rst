MPI main-child application
==========================

We illustrate the concept of a main-child application using our research code ``respy``. As a use case, we are interested in capturing the uncertainties in the model's predictions about average final schooling. For that purpose we start a main process that distributes sampled parameter values from the imposed distribution of the discount factor and the return to schooling.

We can start the script using the terminal.

.. code:: sh

  mpiexec -n 1 -usize 5 python main.py

This starts the main process and allows to create up to five additional child processes.

.. literalinclude:: main.py

The behavior of the child processes is governed in the following script.

.. literalinclude:: child.py
