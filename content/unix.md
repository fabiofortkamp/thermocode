Title: Unix  
Author: Fábio Fortkamp
Date: 2016-01-28  
Category: Article  
Tags: unix, terminal, programming
Slug: unix  
Status: published  
Series: Scientific Computing in Windows

In a [previous post](http://thermocode.net/blog/terminal/), I've talked about using a terminal in Windows and OS X, including the basic steps like opening a _terminal emulator_. I said that I use a shell program called bash in both systems, and that I try to emulate a Unix environment in Windows.

This posts is mostly a clarification to me about why this matter is so important. Why do I go into all this trouble of configuring terminals in my machines? Why don't I just use what every mechanical engineer use?

First, let us talk about what I do in my computer. In my PhD work, I require a computer to do two main things:

* Create programs that do calculations for me. As I've talked about before, my current work involves calculating magnetic field in a region surrounded by cylindrical magnets. I solved Maxwell's equations for my particular geometry and obtained an expression $\vec{H}(x,y)$, where $\vec{H}$ is the magnetic field vector. This expression depend not only on position, but on geometrical and material parameters. So what my program does is to read these parameters from a file, generate values of $x$ and $y$, apply the $\vec{H}$ expression to these values, and store the results in another file, so it can be analyzed.
* Write papers and reports. The results from the above item must be communicated. A PhD studen routinely writes papers (I have one in preparation at this moment), must pass a Qualifying Exam, must write his thesis etc. Since these texts has lots of math, I write in LaTeX, where I can write something like `\alpha` to generate $\alpha$.

Of course I use a computer do other things, like email, but these activities are the core of my work.

What would be the "easy" way of doing this, if I did not want to worry about any of this terminal thing?

For the purposes of this article, I will talk about doing these things in Windows, since I'm focusing on the "common usage" scenario.

## Creating programs in Windows

The standard pratice in the academia (at least for engineering) is to use MATLAB. I've used MATLAB a lot in my life, and I like it. Many of my colleagues have written great MATLAB programs that do all sorts of calculations, and solved important problems in our engineering projects. I've used it for my Master's thesis.

To write programs in MATLAB, you open the "MATLAB Desktop" application, and from there you can use the shells and create, edit and run files etc. In this sense, MATLAB is very Windows-like: to use it, you open a single program where you do *everything* related to that program. It's a closed environment; you use it, and only it, to work on MATLAB "stuff". It's similar to Word, for instance, where you open the Word *application* and from there you write, edit, print. In programming parlance, we say that MATLAB is an IDE (Integrated Development Environment).

What is the problem with it, then?

1. MATLAB is a proprietary program, meaning it requires payment to use it. Because of that, many sites usually have few licenses, or licenses to old versions, or  no license at all. Oh, and any external library requires a separate fee. Call me crazy, but I don't like the idea that, in a few years, to revisit and run the programs I created during this important stage of my career  will require me to pay (or to work on a place that have MATLAB licenses)
2. As a consequence of the above point, there are not as many users out there as I would like. When I reached a complex problem in MATLAB, my best luck was to find an old forum post with few answers. The MATLAB [Stack Overflow](https://stackoverflow.com/questions/tagged/matlab) page was not very helpful when I needed it.
3. It's is not a full programming language. It excels at generating matrices of data. But then I reach the not-uncommom task of storing and organizing these matrices into files, separated in directories. This simple task is very hard to achieve, as MATLAB's interface to the operating system is poor. Besides, its capabilities of working with text instead of numbers are primitive. 
4. The Desktop application is not keyboard oriented. I like to feel efficient in my work. More about this in a minute.

So I don't want to use MATLAB. Python is a good alternative, and its scientific computing capabilities are always growing, mainly with the usual suspects: numpy, scipy, pandas, matplotlib, ipython. Plus, contrary to MATLAB, it's plain easy to create files and folders and to manipulate text. The syntax is as easy as MATLAB's. What is then the easy way to use *Python*?

You can go to the [Python website](http://python.org) and download a [Windows installer](https://www.python.org/downloads/windows/). This will install a terminal emulator to run the Python shell and a simple IDE called *Idle*, which you be the equivalent of the MATLAB desktop application. I could develop my Python programs (to solve my real PhD problems) in this IDLE program, but I would still hit point 4 above.

When I work on my program, I work on two files: my main script (which does the calculations) and a test script, that basically runs the main script and check that it's doing what it's supposed to do (and that no error occurs). So, in a typical work session, I open the test file, run it, and based on the results (error messages) I edit the main file to "satisfy" the tests. When everything is working, I expand the test script and repeat the process. I also have to effectively *edit* the files: search for typos, change the name of a variable in *all* places it appears, change the identation of some regions. These tasks, in an IDE, normally require a lot of clicking or some awkward  non-configurable keyboard shortcut. This can be very annoying and disturb my flow of work. There is a better way.

Under the Unix philosphy, there are some principles:

* Break a complex task into single taks that can be performed well by a single program
* Always try to work in terms of text
* Use the shell to guide your work.

So how do I work on my Python programs? I open bash and navigate to where my programs live. I then use [Emacs](https://www.gnu.org/software/emacs/), an ugly, classical, difficult and powerful text editor to *edit* my files, doing all sorts of text transformation. When I'm done, I return to the shell, and from there I run the Python shell and the test suite. Based on the results, I return to my editor and continue to work. Everything is done through keyboard shortcuts (beginning with the classical `Alt-TAB` to switch the terminal emulator and the editor). And since I am always working in the shell, I can do easily file manipulations, like copying and deleting files, using a version control system.

What's the beauty of this? Now suppose I want to work on a paper; what do I do? You guessed it: I open bash and navigate to where the paper LaTeX files live. I open emacs, edit the file, and run the LaTeX compiler (actually, I use a plugin for Emacs that does this automatically, but I use the shell when in doubt). Emacs is not a Python editor or a LaTeX editor, it's a *text* editor, and it's very customizable. There's an awesome package called [AUCTeX](https://www.gnu.org/s/auctex/) that is simply magic. If you know LaTeX and use some crappy free LaTeX editor, just be aware that I do not type any of that `\chapter{}`, `\begin{figure}` etc boilerplate. I press some keyboard shortcuts (completely ingrained in my muscle memory) and it does that for me, just prompting me for the title and other parameters. You can also create your own commands in Emacs; I'm still learning that.

In short, this is why I use terminal emulators and spend some initial time configuring it, so that my work during the day is smoother. John D. Cook recently wrote [a great article](http://www.johndcook.com/blog/2015/12/22/automate-to-save-mental-energy-not-time/) pointing out that we automate to save mental energy, not time. For me, using Unix in Windows is like this: I've known the Unix model of working, so I try to emulate it in every machine. I use the command line as a track, from where I do my work. If it involves text (as most taks do), I open my text editor, and spend some time learning shorcuts for that particular language/use. I then *do* the work in the text editor, and use the shell to auxiliate me. When I'm done with this project for the moment, I close all files, and return to the shell to navigate to somewhere else. If it does not involve text editing, I *try* to make it about text editing, or I learn how to operate everything from the command line; if I'm working in a Jupyter notebook, for instance, I go the folder, run the Jupyter server from the shell, and work on the notebook in the browser; when done, I return to the shell, clean files, check in to the version system, and move on.

Using Unix and these ancient tools means that, once you get into this workflow of "navigating through the shell and editing files", you spend more time creating and less time clicking.








