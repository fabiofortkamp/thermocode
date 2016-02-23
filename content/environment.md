Title: Environemnt variables in Windows  
Author: Fábio Fortkamp
Date:
Category: Article  
Tags: unix, windows  
Slug: env  
Status:

Jupyter series

If you are one of the people who read this blog, you may have noticed that a recent obsession of mine is the mixing of Unix and Windows. As I've said a couple of times, I've been moving from an Apple-only system to a more diverse environment (primarily due to portability and cost reasons). Today, my main use case is Windows and Android. However, in this move, I've been bringing my Unix experience to try to enhance the use of Windows for programming and scientific computing, and I've been surprising myself with the results. Expect this to become a regular theme here.

I've also notices that Windows users are not so much experiencing with this Unix philoshophy, contrary to Mac users. Hence, in the following texts I will talk more and more about how to configure Windows to do all sorts of things, in the hope that OS X users will know to find their way. I cannot try to cover both systems for every topic I write about. Also, I try to cover concepts and not so much specifics of platforms.

This series about Jupyter is my guide along the way. For me, the power of using Jupyter on Windows comprehends the power of using Unix. In the last post, we talked about using the terminal as an interface to the operating system. You type commands, a shell interprets them and sends the command to the processor, which executes the task - mainly manipulating files in our examples. Today we will talk about opening programs and the shell finds them.

I'm assuming you have already installed Git for Windows and know how to open the Git Bash terminal. You may have to choose something about "setting the PATH", and that will come to our attention again when we install and Python and Jupyter. What is that?

The PATH, is an *environemnt variable*. It's a global configuration hat changes the way your computer works. In the case of PATH, it's a list of directories that Windows searches for when you request a program. For example, if open a terminal (any terminal, including `cmd.exe`) and type the name of a program such as `rm`, how does the shell knows what to do? It cannot possible look in every folder in your computer as this would take forever. It searches for files names `rm.exe` (since that's how programs are named in Windows) and if it finds one, it executes the program.

Naturally you can call the `rm` program even if it's not in the PATH --  you just have to specify the full path (the adress in the file system, not the environment variable). For example, if `rm` is installed as `C:\Program Files\Git\usr\cmd\bin\rm.exe`, and this directory is not listed in the PATH, typing `rm` will not work, but typing the whole path will. It's not practical to type this every time you want to call a program, so it's easier to first configure PATH and hen jsut calling `rm`. It also allows the creation of scripts that use the `rm` command that could be called by bash on both Windows and OS X; if the PATH values are correctly set, the script does not need to know where to find programs, as it passes that job to the shell.

If you type the name of something that is not a program in that path (and is neither the name of something supported by the shell, such as aliases, functions or builtins, but that is not important now), you may get a message like `command not found` in bash or `<...> is not recognized as an internal or external command, operable program or batch file`. If you are sure that you install such program, then it's time to tweak the PATH environment variable.

Since I'm used to Windows 7 but there are newer versions, I will leave you with links on how to alter the PATH (and other environent variables) on these versions

Links Win 7, 8, 10

Hence, when you read something about changing the PATH, or that you cannot call some program from a shell, try first to see if the PATH is correctly set. Also keep in mind that there the "system" PATH, that is set internally by Windows, and the user PATH. This is what you must alter.

The order of directories in the PATH list is also important. The shell will look for programs in the directories in the order they are listed, and executes the first found. This is useful for keeping multiple versions of programs installed, with one as the default. To access the other, you just have to type the full path. the first one, which is the default, is what will be called most of the times, and you can write scripts that say just `python`, for instace, instead of specifying the full path.
