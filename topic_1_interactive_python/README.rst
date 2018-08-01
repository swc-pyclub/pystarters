How to handle packages (for the uninitiated)
============================================

Question 1: What is python and what does it do how does it work please help me
------------------------------------------------------------------------------

Python per se is a language (understand a grammar). Most of the time when we talk about Python, we actually talk about cpython, the C implementation (i.e. the file that reads the code you write is written in C). When you type 

.. code-block:: bash

  python my_project/my_test_file.py
  
on your computer, you are calling the python interpreter. This is a program written in the C language (see above) delivered as a compiled executable (e.g. python.exe on Windows). This program will read your source code (the .py file) and translate (i.e. interpret, hence the name) the instructions in it for the CPU which will execute them.

If your program needs libraries (has import statements) to work, the python interpreter needs to locate and extract the instructions from these files (these are .py files too). The neat (and maybe confusing) thing is that the interpreter first looks within a specific set of folders that are located in the same directory (before exploring other specified locations). This means you can have multiple instances of python (i.e. the interpreter and its folder of libraries) installed on the same machine with no problems (or lots of problems depending on whether you are familiar with the contents of this tutorial or not).

Whenever you make a call to python, you are in fact calling the full path to that python executable file implicitly. 

.. code-block:: bash

  /Users/somebody/wherever_python_is_installed/python.exe

“But wait can’t I just type `python my_code.py` into terminal and it works”. This is true, but only because your operating system knows where to look for that specific python executable file. It does this using the system variable called PATH. What is in the PATH variable determines the order of locations in which your computer will look for anything with the name python (in this case). You can modify this if you want. Anaconda will modify it for you when you install it such that conda takes preference.

If you want to check which python/ipython/pip/conda you are using (from terminal) you can use the following command:

.. code-block:: bash

  which python
  which ipython
  which pip
  which conda

If you want to see the order of the directories that your computer will check when you try to run python in terminal:

.. code-block:: bash

  echo $PATH

Question 2: What is a package?
------------------------------

Okay great so python is an executable and I can have loads of pythons slithering about everywhere in my computer, I can use it to run my code, why the hell should I install anything else at all. HAVEN’T I DONE ENOUGH ALREADY?

Answer: No, you haven’t done enough.

Suppose I want to run my super important analysis module called super_important_analysis_module.py. 

In principle we can do this by executing the following command in terminal:

.. code-block:: bash

  python super_important_analysis_module.py

However, in this way we are only able to run this code when we cd to the directory that the code is saved in. If I want to call any of the super important analysis functions or classes from another location, I would have to manually direct Python to look into the folder that contains the .py file. It would be much more convenient if I could just import these super important functions and classes like this:

.. code-block:: python

    import super_important_analysis_module


Fortunately, there are tools for this. They are there to make this as pain free as possible. It is not a manual task, but it is good to know how it works (so that you can debug the process when it doesn’t work).


In the beginning we had to get our hands dirty: 
***********************************************

- Manually download the package you want to use
- Open a terminal
- cd into the folder, where you should see a file called setup.py
- Run the following command in terminal: 

.. code-block:: bash
  
  python setup.py install
  
This creates an installed version of the same code in site packages, meaning that from now on, Python knows where to look for the code, without us having to tell it where to go. 
Note: running python setup.py install will make a copy of all code into a subdirectory of the directory you installed Python in called site-packages. This means that you can safely delete the original folder in the location that you downloaded the package in.

Then we automated some stuff to make life easier
************************************************

This is obviously tedious.exe so some people made pip: a tool that makes it very easy to install Python packages. Pip takes care of both the downloading and installing of Python packages. It can automatically download the packages from PyPI – a database containing pure python code (most code you will want to use can be found here).

Assuming the super_important_analysis_module.py is on PyPI, we just need to run:

.. code-block:: bash

  pip install super_important_analysis_module

This will complete all the steps in the first example and is even polite enough to delete the downloaded code from your machine so that the only version is in site packages.

Then conda covered up the holes
*******************************

However, pip is limited for a few reasons: 

- Pip doesn’t manage dependencies well
- Pip doesn’t manage non-pure python very well (i.e. executables etc, necessary for nice platform agnostic stuff that maybe isn’t relevant yet)
- No environments (kind of)

Fortunately conda came to cover up the holes and most people were fairly pleased with it. Conda is a cross-platform package and environment management system, and it is extremely useful for handling dependencies, non-python software, and environments.

Side point:

Since you can have multiple versions of python, each with a different installation, it is likely that you will have different version of a given package installed in different places. You can always check which package you are using (and where it is installed) by typing the following into a python console:

.. code-block:: python

  import the_module_i_want_to_check
  print(the_module_i_want_to_check.__file__)

You can also check the path variable that tells you all the places that the running python console will look when you try to import something:

.. code-block:: python

  import sys
  print(sys.path)

With these simple tools you should be able to troubleshoot common issues that you may encounter when importing or installing packages.


Question 3: what is a dependency???
-----------------------------------

All code requires other code. Code that is required by code is a dependency. Anything that you import into your code is a dependency. Sometimes you just need the package, other times you need a specific version of a package. The more specific the requirements the deeper the rabbit hole, the messier it gets. A particularly annoying situation is when you have multiple softwares that require different versions of the same package: Upgrading to the newest version means your old software won’t work anymore, but staying with the old version mean your new software won’t work!

Question 4: How do I make sure I never have to worry about this very worrying problem that has been outlined above??
--------------------------------------------------------------------------------------------------------------------

Conda environments were built for this. If you are worried that installing something might break something else then it is time for a change of environment.

An environment is a complete python directory, with its own set of site-packages (remember this is just a directory that contains all of the installed code that the specific version of python that you have chosen to execute will look at when you ask it to know what the hell numpy is (for example)).

You can create as many environments as you want, but you have to be very specific when you ask your computer to run python (you should say which python you want to run). This is all neatly handled by conda:

Create an environment

.. code-block:: bash

  conda create -n my_super_cool_env

You can then activate it (Windows users leave away ‘source’):

.. code-block:: bash

  source activate my_super_cool_env

and any installation or python commands you use will refer to this environment only. In other words, if you call Python when in that environment, only the Python version and packages that you have installed in that environment will be available to you. If you want to go back to your base python, you type: 

.. code-block:: bash

  (source) deactivate my_super_cool_env


Question 5: Okay that’s cool and all, and I’m sure I’ll be super happy that I did this at some point but isn’t there some less annoying way to do all this. Maybe some sort of dedicated coding environment that kind of knows what I want even when I am not sure myself?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Yes. PyCharm. All you have to do is set the interpreter (this is just a fancy name for the particular python executable that you want to use). This is under project interpreter in settings. Pycharm automatically detects when you are trying to use a package that is not installed, and you can install them with a right mouse click. 

