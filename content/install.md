Title: The mechanics of programming languages  
Author: Fábio Fortkamp
Date:
Category: Article  
Tags: programming, unix, windows  
Slug: install  
Status:

What does it mean to "install a programming language"?

As we talk about creating a scientific programming environment in Windows, we'll eventually need to install Python, LaTeX, R and some other programming languages. But of course this is a figure of speech, as we cannot install a concept like a programming language -- only the tools needed to work with it.

One of the things that annoys me to an extreme about programming text is that how they ignore and skip convering what I like to call the *mechanics of programming languages*. For example, if you want to work with Python, before you even begin to study variables, for loops, lists, classes etc, you have to know the very basics. What do you need to write a Python program? How does Python work on your machine? And how about writing in LaTeX? What's interesting to me is how this idea is linked to Kourosh Dini's *Workflow Mastery* (which I also cover frequently here) and its idea that "much of the mastery is a mastery of the basic". 

For me, the mechanics of a language comprise {?} these steps:

1. Installing the interpreters/compiler/resources for your programming language of choice
2. If possible, running an interpreter/shell
3. Executing/running a program/script
4. Installing extensions
5. Creating extensions

As examples and clarifications, I will cover the mechanics of Python and LaTeX, my most used tools.

## Using Python on Windows

Python is an interpreted programming language, which means there is a Python shell that can execute a command line or loop through a script and execute all lines to create a program. In my opinion and to paraphrase Kourosh Dini, "much of the mastery" of Python is about understanding that the difference of a Python script and the Python interpreter is much a matter of convenience.

To work with Python, then, you need the Python interpreter. There's an official Python installer, that install the `python.exe` that you can run thourgh the terminal and include some extras: an IDE called IDLE, where you can write basic Python scripts and run them from the editor, and Windows feature such as associating `.py` files with the `python.exe` program. This official installer is fine to learn Python, but as soon as you install lots of extensions the process is cumbersome, as usually each library will have its own installer that you have to download.

A much better way of using of using Python in any platform is the use the Anaconda system. Anaconda is a *distribution* of Python that includes the interpreter, lots of scientific programming libraries pre-installed and ditional command line tools that facilitate the work a lot. To install, download the Anaconda installer (I'm using version 3 and haven't had any compatibility issues in a long time - CLARIFICAR) and install like any other Windows program. If you don't have any other version of Python installed, everything should work fine; otherwise, check your Path to see if the directory of Anaconda is before any other Python system such that, when you type `python` on the terminal, you run the Anaconda version.

Speaking of that, get used to open a terminal and typing `python`. The is the core Python shell, where you can execute commands. After you launch the interpreter, you see a message showing the version (the string `Anaconda` should be in it) and then the `>>>` prompt. Now you can type any valid Python 3 statement, like

	```python
	>>> print('Hello, world!')
	Hello, world!
	>>> x = 2
	>>> x = x + 3
	>>> x
	5
	```

For serious work with Python, there's an enhanced shell called IPython, which is included with Anaconda and which you can launch with `ipython`. Refer to the documentation to learn about its features but, if you are just starting, you can use the standard shell to simplify things.

{syntax highlighting for inline code?}

The Python shell is a process launched by whatever shell you are using to type `python`; I'll assume it's bash. When you launch `python`, the interpreter is using as working directory the directory where it's lanuched from. To execute a script called `calculate.py` located in `~/code/python-script`, then, you can either type `python ~/code/python-scripts/calculate.py` or navigate to that directory and running `python calculate.py`.



## Using LaTeX on Windows
