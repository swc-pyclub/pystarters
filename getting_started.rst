What you will need to set up before you start
=============================================

PACKAGE MANAGER
---------------

We recommend using Anaconda or Miniconda for managing your python environments and packages

1) Install miniconda from: https://conda.io/miniconda.html

Once you have done this, open a terminal window and type:

.. code-block:: bash

    conda help

This should display conda's documentation help. If it does nothing then something has gone wrong.

2) create a conda environment for this course

This is useful because it will keep all of your python packages encapsulated from your system. It means that if you break something then only the environment will stop working rather than your system python. 
There is a full guide here: https://conda.io/docs/user-guide/tasks/manage-environments.html

To create an environment for the course:

.. code-block:: bash

    conda create -n pystarters_env python=3.6

Every time you want to use it, you need to activate it:

.. code-block:: bash

    source activate pystarters_env

TIP: if you are on windows you don't need to write source


3) Use conda to install some of the key scientific packages to your environment (i.e. do this once the environment is activated)

.. code-block:: bash

    conda install numpy scipy matplotlib jupyter



JUPYTER NOTEBOOK
----------------

To open a jupyter notebook open a terminal window and type

.. code-block:: bash

    jupyter notebook

A full guide can be found here: http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html


IDE
---

We strongly recommend using Pycharm as your default python IDE. It boasts many useful features, but is particularly good for inspecting and refactoring code.

You can get it here: https://www.jetbrains.com/pycharm/download/
Get the professional version (it's free for students)

You should then follow the guide for setting up your first python project: https://www.jetbrains.com/help/pycharm/creating-empty-project.html

GIT
---

We highly recommend following the courses using git (there is a git tutorial in week 2 that should help get you started)

1) install git on your machine: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

.. code-block:: bash

    git clone https://github.com/swc-pyclub/pystarters.git

