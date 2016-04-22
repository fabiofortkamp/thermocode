Title: Scientific programming in Windows  
Author: Fábio Fortkamp  
Date: 2016-04-18  
Category: Article  
Tags: programming, python, Jupyter, Windows, Unix  
Slug: sciprog  
Status: published  
Series: Scientific Programming in Windows  

When I [started][jupyter-first] this series on [Jupyter][jupyter-site] notebooks, I wrote it was "my most used tool" and that I think its installation and usage for Windows users may not be very straigthforward.

As [I've written before][terminal-post], I learned to use Linux when I was taking CS classes in Portugal, and I learned some key concepts that changed the way I use a computer. I learned that every task you perform at your computer is translated into calls (instructions) to the operating system; when you select a file (say, `file.txt`) in your Desktop and hit the `Delete` key, the OS finds the portion in the storage area (your SSD or HD)  where the file lives and frees that slot. With terminals and shell programming languages, you can interact with the OS bypassing the graphical interface, by typing `rm ~/Desktop/file.txt` into a terminal. I learned to use Bash and I fell empowered with it.

I also learned the concept of processes. As I understand it, a program is a file that sits in you computer, and a process is it loaded into (RAM) memory and running. In more practical terms, I learned you can you can use the shell to launch processes, and that you control (or change) this act by passing arguments to programs. For example, typing `python` in a shell will launch the python program, but typing `python -I` will run the interpreter in a different way. To take advantage of that, good UNIX programs have good terminal interfaces; in particular, a program may take textual input and return textual output, or read an input file and write an output file. Typing `python` will launch the interpreter with its shell, where you can type commands, but typing `python my_script.py` is equivalent to opening the interpreter, making it read your program line by line and then exiting the shell. What is really brilliant about this is that the hard part is making Python read a line of code and interpret its content; once that is done, making it loop through a file becomes easier. 

These notions can be very liberating. For example, when writing LaTeX (by far, the things that occupies most of my time right now), it helps to know that LaTeX works by typing `pdflatex paper.tex` into a shell, having as a  result a file usually named `paper.pdf` in the same directory. Knowing this, you are not tied to a particular LaTeX editor, because you know that it's just a matter of editing a source file, running a command (or just a few more, to get bibliographies and indexes), and getting a PDF as output. If you learn that `pdflatex` also takes arguments, you can configure any editor, by just tweaking this command. When you learn this kind of basic usage of the terminal, you can understand that your editor is just a front-end, and that you can configure everything. Suddenly, LaTeX is not magical, but rather a program that reads a text file and produces a binary file (PDF).

These concepts are not familiar to Windows users. I think it's not absurd to assume that the prototypical Windows user is the employee of some company doing office work, and enterprise people do not want to open the terminal and pass arguments to commands. They want to have a Microsoft Excel icon in the desktop, in which they click to work on a spreadsheet. When they are done, they close Excel and move on to something else, normally by clicking a different icon. They associate taks with programs, not with files. If they want to write a document, they open Microsoft Word and work from there, and the working file is only either opened in Word or sent by email.

Jupyter does not work that way and does not fit well into Windows culture. Yes, there's an `.exe` file that you can [download to install Python][python-win], but from now on you have to use the command line to install Jupyter, navigate to the folder where you want to create your notebook, launch the notebook *server* etc. Once you do that, you are in a browser window and everything works as expected, but the steps are not trivial. Becuase of that, I started to write these texts, beginning with basics from [what is the terminal][terminal-post] to [what is the PATH][path-post]. I always had this goal in mind, to clarify every step possible in order to work with Jupyter.

Now, however, I noticed that this whole discussion is not about Jupyter notebook. It's about those things I've talked about, about learning to use the terminal, to acknowledge the power of plain text files, and how to modify command line programs. It's about the Python programming language in general, in how it can be a perfect substitute to MATLAB (as [I've talked about][unix-post]) to manipulate numerical data. It's about engineers and scientists who use computers not as administrative tools (to just fill spreadsheets), but who write programs for computers -- but not any kind of program, rather programs that manipulate data, generate plots, perform bulk manipulation of files. To do science, in other words.

Because of that, I'm converting this series on Jupyter notebooks to the broader topic of *Scientific Programming in Windows*, a topic for which I have great interest, and a topic which has been in the news lately -- have you seen that [Windows 10 will have a Linux subsystem *built in*][wls], just so that users can interact with a command line in a more proper way?

I do this kind of work every day. I use Python to write little scripts, I use Jupyter as an alternative interface to Python, I write in LaTeX, I've been using some neat bash scripts. I've been learning to be efficient with scientific programming in Windows, and I want to share my ideas with you. Stay tuned!

[jupyter-first]: http://thermocode.net/blog/jupyter  
[jupyter-site]: http://jupyter.org/  
[terminal-post]: http://thermocode.net/blog/terminal  
[unix-post]: http://thermocode.net/blog/unix  
[wls]: https://blogs.windows.com/buildingapps/2016/03/30/run-bash-on-ubuntu-on-windows/  
[path-post]: http://thermocode.net/blog/path/  
