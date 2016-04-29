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

To emphasize one more time the fact that Python fundamentally executes a line of code, you can simply type `python -c 'print("Hello, world!")'` and the string between `''` will be executed.

To extend Python, you install *packages*, which are loaded into the shell with `import <package name>`. One advantage of Python (compared to other programming languages) is that it has a *batteries included* philosophy, meaning that the Python interpreter ships with lots of built-in packages. One advantage of the Anaconda system (over the conventional Python installation) is that is also includes many third-party packages that are much used in scientific computing. Hence, with the official Python installer, if you type something like `import numpy`, you will get an error saying the numpy library cannot be found. However, if you followed the steps here and installed Anaconda, this statement should work out-of-the-box.

The regular Python system has the notion of an environment variable `PYTHONPATH`, which can be a list of directories that include python packages. Hence, if you would like to use some obscure Python package that you download, you can then modify the shell (I'll not dive into this) to include the directory to where you downloaded the package, and from the same shell launch the python interpreter; it will inherit the environment variables and then, when you try to import your obscure package from your location, Python will know where to find it.

An aside: I'm serious when I said that Python knows everyhing about the shell from where you lanched {Explicar como acessar variáveis de ambiente}

Because Python is open-source, it can be modified and distributed, which means that the Anaconda version of Python works in a different way (this only affects the mechanics, though  the programming language itself is identical). Because of that, the only reliable way of installing packages in Anaconda Python is to explicitly install it with a *package manager*. The Anaconda system provides one excellent called conda. To install a package that is not included in the Anaconda distribution, you can type:

	```bash
	$ conda install docopt # docopt is a library for command line programs that is not included
	```

The `conda` program can be used to installed actually many programs, not just python libraries. Dive into the documentation for more details. A nice touch: you try to install something it does not recognize, it shows a help message indicating what you can do to search for what you want to install.

The Anaconda system also includes the official Python package manager, pip. And again, because of the open source nature of things, the Anaconda version of pip knows what to do to make the package importable for the Anaconda version of Python. To install something via `pip`, type:

	```bash
	$ pip install pelican
	```

Please be aware of the "linking" between programs. You can have several versions of python installed, which it own pip version. Becuase of how different distributions organize their system files, when you install something via pip, it will know where to put the installation files, but they are not acessible. For example, if you install something using the Anaconda pip, but then launch the official Python shell, it may not be able to import something you just installed, because it was placed in a different location! To avoid headaches like this, first and foremost aim for simplicity: try to use the Anaconda system exclusively, and only one version (2 or 3), and check to see if the Anaconda path is placed in the front of other Python paths. In bash, you can also type like this:

	```bash
	$ which python
	$ which pip
	```

The `which` command will try to find where in the `$PATH$` these commands are placed. If the output of these commands are similimar (e.g. they are placed in subdirectories of a `Anaconda3` folder), you should not have any problems.

Also keep in mind that `pip` is a Python package manager, while conda is very general. But because `pip` is the standard (to be used by any Python distribution), you may find something that is not available via `conda` that is via `pip`; that's fine. From a package installable via `pip` to be installable via `conda`, a *conda recipe* has to be created for each platform, and that's why you may not find a specific library (or only an older verion, or only for a different OS) in the Anaconda index. To be consistent, I try to first install using the conda manager, and fall back to pip if I can't find. I haven't had any problems with that. I have yet to explore the power of conda to install other Windows utilities.

Speaking of conda recipes, that's how you can install your own libraries. Hopefully, after a few years of Python, you will begin to create your own functions, and will grow them into packages, that you want to import like any other library. I'm still learning and experimenting in that real, and in the future I may post a tutorial in creating your own recipes; for now you can research the documentation. If you are just starting with Python, you shouldn't worry about this.

**To summarize:** the Python programming language is accessed via a Python interpreter, which primarily takes a line of Python code and executes them. To run a Python program is to call the python interpreter to execute the file line by line. To use the shell in interactive mode, ou need to install the interpreter. There's an official port of Python, but installing packages for scientific computing with that is difficult. Because Python is open source, there are different distributions that include some extra features (without modifying the programming language). For scientific computing, the best one is Anaconda, which already includes popular languages. It includes the pip and conda tools to install external libraries, and conda recipes can be used to transform your own files into importable packages. 

## Using LaTeX on Windows

LaTeX isn't a traditional programming language such as Python (or is it), but I've found that with experience treating writing in LaTeX as writing a program makes me a better writer.

LaTeX is a system for preparing documents. Instead of using a traditional word processor, you write your documents in a plain-text file and embed commands in it. The basic principle of working with this (and the one that I think is most difficult for people familiar to use Microsoft Word) is this *separation of input from output*. The file you work on is not the file that you will send to others as a final product; the latter has to be *compiled* from the former.

I will assume that what you want is to create a PDF document that you send to your boss, professor, advidor etc; for that you need a command-line program called `pdflatex`. As with Python, there are several distributions of the TeX/LaTeX family. In Windows, MikTeX is popular, but because I've used Linux, OS X and Windows at different stages of my professional life, I like to use TeX Live becuase it's cross-plaftorm. So the instructions I use here will assume the use of TeX Live, which you can download and install like any Windows program here. Warning: it's a long installation process; LaTeX is complex.

The intallation process should adjust your `$PATH$` automatically. To test, type in bash:

	```shell
	$ which pdflatex
	```

If the TeX Live directory appears in the output, you are fine, otherwise add the appropriate directory to your `$PATH`. For a default installation, the directory where the executables are located is something like `C:\texlive\<year>\bin\win32`.

Let's say you are writing a report. You create a document called `report.tex` in a folder; to create the PDF version, you type:

	```shell
	$ pdflatex report
	```

If there are no errors, a new file `report.pdf` should be created in the same directory. This is the basics mechanics of using LaTeX.

Unlike Python, there is no "LaTeX shell" for interactive shell. If you type just `pdflatex`, you get a `**` prompt that just waits for you to type the name of the file you want to compile, but you can't do much more than that.

`pdflatex` is just this: a program that takes a file and creates another. Due to the power of the command line, you can configure this process; type `pdflatex --help` to see available options, and go crazy.

{ falar de configurar editores. Exemplo com algum editor? O que eu poderia querer modificar? Mudar o índice}
