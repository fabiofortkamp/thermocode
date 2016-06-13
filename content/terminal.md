Title: Using the terminal  
Author: Fábio Fortkamp  
Date: 2016-01-27  
Category: Article  
Tags: jupyter, terminal, unix, terminal  
Slug: terminal  
Status: published  
Series: Scientific Programming in Windows  

Before we dive into using Jupyter notebooks, I feel obligated to better clarify the terminal. Currently, the only way to use notebooks is via the command line, and I've observed that even engineers with broad experience in programming have no idea what the terminal is, being mostly experienced with IDE-like programs (like MATLAB, or Visual Studio, or most LaTeX editors). To assure everyone interested in running Jupyter notebooks understand what I'm saying, I will try to give a crash course in using the command line.

First, a word of warning: I'm not a computer scientist nor an expert in the subject, but I do have a particular interest in the command line and programming in general. When I lived in Portugal for a year as a undergraduate student, I took some CS classes, which opened my mind to see how we can interact with a computer in a deeper way, effectively *controlling* it. Maybe my lack of experience can help in writing this posts; I don't target professional programmers, but engineers and scientists who do use computer professionally and would like it to more intelligently. What I write here may be not 100% accurate, and has the explicit purpose of helping someone learn the terminal.

## What is the terminal?

Your computer has processors, and they execute instructions. They understand how to manipulate files and programs, which are stored in form of bytes in your hard drive or SSD.  When you open a program (double-clicking an icon in a Windows desktop, for example), the processors will find the program file in your storage system and will load it to the memory (RAM), where it can be used by you (the RAM memory is much faster, but more expensive and volatile, and that's why you have 1 TB of storage and about 10GB of RAM). When you select a file in the file browser and hit the delete key, the processor will locate where the file is stored in disk and will free that area. When you try to raise the volume, the processors will request the audio board to do so. I'm oversimplifying, but you get the idea. Everything you do with your computer is translated to some *command* that the processor will interpret and execute. This is the basic abstraction that we will use in clarifying the terminal.

A *shell* is a program, just like any other in your computer. What it does is to let you type some command, written in a programming language, to execute this command (by translating and sending it to the processors) and to show your back the result (if any). If you are interested in all this scientific computing thing I'm talking about, you are probably familiar with MATLAB, which also has a shell! When you open the MATLAB "desktop" application, you are greeted with a blank window, which shows you a blinking cursor after a `>>` symbol. You then type anything in the MATLAB language, press `Enter`, and if there's a result it will appear to you. The shell then waits for new input, with the same blinking cursor and the same `>>` string. This is called a [REPL (read-evaluate-print loop)](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop ) .

Notice that, to use MATLAB, you interact with it in a textual way. There is no "New matrix" button that you have to click, and no "Plot vector" icon either. You write instructions and the shell execute them. 

Some shells are more speciliazed in operating system tasks: manipulating files, opening programs etc. Like a Portuguese professor once told me, these terminal shells, like animal shells, "wrap around" the low-level operating system and translate things humans understand to things the computer understands.

Shells are of great importance in the Unix world, an ancient operating system which gave birth to two main other families of systems: Linux and OS X (the system of Apple's desktops and laptops). The Unix "philosophy" can generate many posts, but the important thing to understand is that Unix programs (including OS X apps) are usually centered around the terminal, with a graphical interface (GUI) wrapped around it. In OS X there is AppleScript, which (even with all its defects) let you write *your* own commands to pass to the application (like my [little `skim2md` project](http://thermocode.net/blog/skim2md/)). Windows was designed with an alternative philosophy and is much more centered around the graphical elements themselves. What this means is that terminal shells are much more natural in Linux and OS X, and using the terminal in Windows has its challenges. We'll see some workarounds. 

One of the most popular shells in the Unix world is *bash* (the shell that I actually use). To understand it, let us give an example;  say you are using OS X and you want to delete a file named `report.txt` from the Desktop. Graphically, you select and delete it. To do it from the Terminal, you open an application called `Terminal.app` (in the `/Applications/Utilities/` folder) and type this command, followed by the return key:

	:::bash
    rm ~/Desktop/report.txt
    
This will have the same effect as deleting the file. The `rm` command deletes the *argument*, which is what is given next. The character `~` is widely used in shells to denote the *home* directory (e.g. `/Users/<username>/` in OS X), the folder that is associated with a specific user of the computer; `/` is, in the Unix world, the directory separator. Hence, we are invoking the `rm` command, to act on a file `report.txt`, inside a folder called `Desktop`, inside the home folder.

But why? What is the advantage of going into all that trouble? Well, shells use complete programming languages, so you can perform any sort of logic. To delete a single file maybe it's not advantageous to use the shell, but what about deleting only images, in a folder with thousands of files? Or only files that start with `report`? Or files bigger than a certain limit? All of this can be achieved with a single (but sometimes complicated) command. Try to do that by hand.

To summarize: a terminal shell is an interface to the operating system, programmable with some language. The most popular (I guess) is the bash shell, the standard shell on Unix systems (represented currently by Linux and OS X).

## Terminal shells on Windows

Windows users tend to be not so familiar with shells, but there is one (note: I'm using Windows 7, so I'm not sure how all of this work on Windows 8 and 10): the `cmd.exe` shell. Try this: type `cmd` on the Windows Start search box and will get a simple terminal windows with the shell waiting for your response. To be really specific, it's in `C:\Windows\System32\cmd.exe`.

![Windows Command Prompt]({filename}/images/cmd.png)

First of all, for any of these to make sense (and to use Windows a in a more Unix-like way), you may have to [change the `HOME` directory to `C:\Users\<username>\`](http://www.computerhope.com/issues/ch000549.htm) (notice that `HOME` is called an *environment variable*, a parameter that controls the general environment in your computer).

The mentioned program (see how it ends with `.exe`, making it clear that a shell is just a program) also interacts with the operating system, but uses a different syntax than bash.

For example, the command to delete the file above would be

    :::dosbatch
    del %HOMEPATH%\Desktop\report.txt
    
    
The command name is different, the notation for the home directory is different, and the path separator is `\` instead of `/`. The effect is the same, though.

`cmd.exe` is a simple shell and much less powerful than bash. There is a more powerfull Windows shell, [Powershell](https://technet.microsoft.com/pt-br/library/dn425048.aspx), but I've never got the time (or will) to try it out. If you are interested in this and use Windows exclusively, you may want to check this out.

### Bash on Windows

Since I learned to use the shell when I used Linux and I still use OS X, I'm much more used with bash, and I would like to be able to use it on Windows. Luckily, there is a solution -- actually, two solutions.

The more complete is [Cygwin](https://www.cygwin.com/), which is a collection of Unix utilities written as Windows program. So you would install Cygwin, use the bash shell that comes with it (check the documentation on this), invoke the `rm ...` command shown earlier, and bash would interpret this in a way that the Windows operating system can understand. For years, I used Cygwin and was OK with it. It works fine but is limited by what the operating system can actually do. Windows is not Unix.

The problem I got with Cygwin was when trying to  use Git. Git is a version control system, which I will not cover here in this post --  just keep in mind that it's a command-line program that keeps track of changes in your projects, both on your local machine and on a remote repository (like [GitHub](https://github.com/),  mentioned in the [last post](http://thermocode.net/blog/open/)). When I'm satisfied with my work and want to *push* the project's version on my machine to the remote server, this happens through a HTTPS protocol, which requires some authentication. When using Cygwin, I got all sorts of issues, and some internet searches  showed that sometimes using this secure connection with Git and Cygwin can be in fact a mess.

Fortunately, there is a project called [Git for Windows](https://git-for-windows.github.io/), which takes care of this. When you install it, it configures a Windows-native Git system for you, and a basic but functional bash shell is included with all Git hooks. When using Git for the first time, I had to type my password, and after that I never had any issues. I'm *very* happy with it.

When you install Git for Windows, make sure to make it a complete installation, choosing to install all Unix utilities and adding them to the PATH. After that, a `Git Bash` program should be available in your Start menu. This is the shell with which you can use a mini-Unix environment in Windows. As we'll see, the easiest way to use Jupyter on Windows is to use a combination of both bash and `cmd.exe`.

## Shells on OS X

Like I said, OS X is Unix, so everything should be pre-configured for you. Your computer already has a terminal, called `Terminal.app`, located in `/Applications/Utilities` (at least in OS X Yosemite).

![Terminal on OS X]({filename}/images/terminal-osx.png)

If you are starting with this, open the Finder in the above folder, locate `Terminal.app` and drag it to the Dock to create a shortcut for easy access.

## Shell vs terminal

Before we continue, we must differentiate between a shell and a terminal, which I have been using in this text almost as synonimous. A shell is the command-line interpreter, like I said. A terminal emulator, or console, is a different program which displays the shell for you.

This is more important than you think. Open `cmd.exe` on Windows and try to select some text. You can't, right? The *window* that you see, a terminal window displaying the `cmd.exe` prompt, is too rudimentary. 

This means that you can use *terminal programs* configured with any *shell* you like. In a future post, I will detail exactly which terminal emulators I use and how to configure; but if you are just starting, I recommend that you just use the Git Bash terminal (which is a terminal emulator wrapped wrapped the shell) on Windows or Terminal.app on OS X. To repeat myself: create shortcuts for them and be aware of them when I say, in future posts, to "open the terminal and...". These programs is what I mean.


## Using the shell

Let's say you configured your shortcuts to the terminals (using bash) and now you have a command window in front of you. Now what? Most shells follow the so already mentioned REPL pattern: first, it *reads* your input; then, it *evaluates* it, then it *prints* whatever the result of the evaluation was (if any), then it repeats.

When you open a terminal with bash, it will exhibit something like this (my prompt on the above figures was customized, but I won't dive into that now):

	:::bash  
	fabio@MacBook$ #<blinking cursor waiting for you to type>  

The text on the left-most side is the prompt, a message that the terminal shows to you when it's ready for input. It's common for shells (and shell users) to configure the prompt to end with a special chracter (like `$` or `>`) to denote the end of the prompt. The shell will read everything you type at the right of the prompt, up until you press the `Return` (or `Enter`) key. It then will interpret and execute the text you send it. After it's done, there may be a message to be printed out. For example, in bash, if you type `ls`:

	:::bash  
	fabio@MacBook$ ls
	
and press `Enter`, it will show a list of files in the current folder. This list will be printed in the terminal windows, so you can inspect it. By "current folder", I mean the *working directory*; at each instant, the shell is acting on one directory. To find out which one, type `pwd`.

This post is already getting too big and I want to focus on what means to use the terminal and on practical things not usually covered (like opening terminal emulators and what prompts are). If you are interested in learning more, there are plenty of resources to be found. I don't remember how I started, but [this guide](http://matt.might.net/articles/basic-unix/) seems nice.

## Next steps

I felt the need to write this big clarification of using the terminal, so that I can talk about configuring and installing Jupyter. If you search the docs, you will see a lot of references to stuff like this, and I'm afraid that not everyone could follow. I hope this makes things more clear, and it's a documentation of some steps needed to configure Jupyter notebooks starting from zero.


Next, we will use the terminal to install and open jupyter notebooks. In the meanwhile, take the time to practice the basics: opening the terminal, navigating through it, executing commands etc.

Naturally, the terminal is useful not only for working with Jupyter. Like I said in the beginning, using the terminal leads to a greater control on your computer, so that you spend less time clicking on things and more time thinking and creating.
