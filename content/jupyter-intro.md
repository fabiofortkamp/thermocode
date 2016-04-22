Title: Jupyter notebooks: my most important work tool  
Author: Fábio Fortkamp  
Date: 2015-11-19  
Category: Article  
Tags: jupyter, python, programming, latex  
Slug: jupyter  
Status: published  
Series: Scientific Programming in Windows  

Without a doubt, [Jupyter notebooks](http://jupyter.org/ ) 
 are my must used and most powerful work tool at this moment in my Ph.D. work. This technology revolutionized the way I write code and solve  mathematical problems, in a way that helps me think and is "pleasant" to read (to the extent where reading equations can be pleasant).

Here is my present use case. In the mathematical model I'm trying to investigate, there are two magnetic cylinders and an air gap between them, and I want to calculate the magnetic field inside this gap. The canonical way to do that is using [Maxwell's equations](https://en.wikipedia.org/wiki/Maxwell%27s_equations ) 
, but I, as a mechanical engineer, am not too familiar with those. So my first task was to grab a bunch of textbooks on electromagnetism and make notes on this subject: what is the magnetic field, what is magnetic induction, what do Maxwell's equations mean, how to model permanent magnets. As any sane engineering student, I use LaTeX to write these notes (and Markdown, actually, but LaTeX is what is used for equations).

After that, I adapted Maxwell's equations to my situation and used differential equations methods to arrive at a system of equations -- but a system of *symbolic* equations. I don't know numerical values for my problem yet, so I have to solve the system in terms of generic variables. Hence, I can't use any numerical methods (which is where computers are really good at), but there is software that can solve symbolic systems. I finally decided to try out Python [`sympy`](http://www.sympy.org/en/index.html ) 
 library, which worked great. So I wrote a little Python program that solved this system.

I now have an expression that allows me to calculate the magnetic field in my region of interest. Time to create a graphical representation! I created another Python script that takes the expression output by the first program, insert some sample numerical values in it, and uses [`numpy`](http://www.numpy.org/) 
 and [`matplotlib`](http://matplotlib.org/ ) 
 to plot the field.

These three things I described -- notes in LaTeX about the theory, a program to solve the symbolic system and a program to plot the solutions -- are actually one single thing, a Jupyter *notebook*, just like a notebook for a math-like class, with text intermixed with solution to exercises. When I work on the code, I can review my notes for better clarification, and when I add new notes I can right away write code that represents, or solves, or plot the relevant part.

These notebooks are then sort of special files (with extension `.ipynb`, because they evolved from [IPython](http://ipython.org/) notebooks) which can store these multiple types of data. On your computer, you go to the folder where you store them and run a special kind of software, a *server* (I'll explain how I configure and use them in future posts). Then, you open your web browser (yes!), at the adress provided by the server, and from this web app you work on your documents. Your browser then becomes an interface for your notebooks; they send commands for an interpreter to execute, and displays the results in a graphically way. 

But why do I like them so much? Why have I begun to use jupyter notebooks in the first place?

(I intend to make this a series on Jupyter notebook, and I'll explain how I use them. But if you are interested, [here is a list of some interesting examples to get started](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)).

## Combination of my favorite markup languages with my favorite programming language

I can't imagine myself writing a Word document longer than two pages (actually, it's been years since I opened Word to write something relevant). I **love** LaTeX, and I consider it one of my essential skills. I still have much to learn, but to be honest, in my social circles I know few people who have studied it and know it better than me. To be able to represent any complicated equation with just plain text actually helps me organize my thoughts.

I also like Markdown, which is much more lightweight than LaTeX, but is not suited for math. With Jupyter, I have both tools at my hands: the notes I talked about earlier are written in Markdown, with things like `*italicized*` to produce *italicized* text, and `# Title` to produce section titles. But thanks to [MathJax](https://www.mathjax.org/ ) 
, I can write equations in LaTeX. And Jupyter includes some tools to convert this combination to a full LaTeX document (which can be processed to produce a PDF report, for example).

As for the code part (for example, plotting a solution), Jupyter has support for many programming languages. I learned to use Python a few years ago and I think is the best general purpose programming language, and has fantastic libraries for scientific programming (operating on matrices, reading and writing text files, doing mathematical calculations, plotting). Since Jupyter notebooks run on web browsers, the graph produced by a plotting procedure can be displayed by the browser like an ordinary figure. Some tabular-like data types from the [`pandas`](http://pandas.pydata.org/ ) 
 library are even displayed as HTML tables (this shocks me every time I use it).

Although I've never studied it in depth, I am fascinated by the idea of [*literate programming*](*literate programming* ) 
, which advises writing programs like essays, where the code is part of a much greater scheme. Maybe not formally, but Jupyter notebooks allow precisely that: I write code after I clarified to myself what that function needs to do, and I can add comments (and formatted ones, with tables and figures etc) right after a figure is produced. It is almost like a complete paper with all computations included, and so it favors another interesting idea, of [*reproducible research*](http://www.jstatsoft.org/article/view/v046i03 ) 
.

## Cross-platform

As [I said in an earlier post](http://thermocode.net/blog/tech/ ), I use a Windows PC at the university and my MacBook Pro at home. To prevent mental stress, I try to use as many similiar applications between systems as possible, so that I make my work truly platform-independent.

When I work on a Jupyter notebook, I work on Chrome (which is my browser of choice) on *both* systems. Sometimes I even forget on which platform I'm working on, because the interface is the same -- I'm just seeing Chrome.

This might seem a detail, but this sort mental stress is a true problem. Whenever I'm working on a notebook, be that on Windows or Mac, the interface is the same, the commands are the same, the keyboard shortcuts are the same -- this is a *very* big deal.

## Dynamic

By dynamic I mean that programming with Jupyter notebooks require a different work method that writing traditional scripts.

Suppose I'm creating a function to calculating something, but I'm not sure about how to use a python command -- what are the arguments? What does the function return? No problem. Jupyter notebooks are split in cells (kind of like Excel, but more appropriately like Mathematica). If I'm writing a cell and I'm not sure how to proceed, I exit my current cell (and it's left there untouched, waiting for me to finish). I create a new cell, and use the awesome [magic](http://ipython.org/ipython-doc/dev/interactive/tutorial.html#magics-explained ) 
 commands to find help for what I want. Then I return to the previous cell and finish editing.

The whole concept of a "notebook" is very important. Once you write then, all your snippets and notes are there, including the errors you made (they do not affect you other cells, as you simply don't need to evaluate the erraneous cell). It becomes a live record of your work session. This dynamic way of working encourages experimentation. You write notes, and then you write a small piece of Python code, and then test it. Then you write another piece of code, and then another. When you open a notebook to work on, you can focus on a specific section, and evaluate the code there. At the end, if you organized your notebook and everything is finished, you just execute an "Run all cells" command and it's like a complete, commented Python program (don't worry, I'll explain all these little details in other posts).

## GitHub renders automatically

This has always been a problem for me. Previously, when I want to show my advisor some calculations I've made, I had to save the figures, or then produce a simple report, and then call him to come to my office. If there was a problem, I has to explain to code to him, and wait for suggestions.

Now, this notebook I'm working on is hosted on a private repository in [GitHub](http://github.com ) 
, and this incredible service can render notebooks as HTML pages. Hence, he (and other people on my project) can just open the repo page (with a right permission access) and check my progress. 

This has the "benefit" of encouraging me to work harder, since my work is then publicly available  (to the people in my project, at least), and this "open" philosophy (much like the ideas from [*Show you work*](http://thermocode.net/blog/welcome/ )) is very benefical to me, I think.

## OK, how do I use them?

Wait for the next post on this series! I will explain everything, from how to configure and use them to some tips I've learned.
