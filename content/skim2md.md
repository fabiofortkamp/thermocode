Title: skim2md  
Author: Fábio Fortkamp
Date: 2015-09-04  
Category: My scripts  
Tags: skim, applescript, reading  
Slug: skim2md  
Status: published  

As part of my Ph.D. work, I read *a lot*, especially PDF files with books, theses and papers.

I've developed a nice routine for this. I sit down on my nice chair, with my MacBook Pro on my lap, with a glass of water on the side and Spotify playing some classical music. I use [Skim](http://skim-app.sourceforge.net ) as my main PDF reader because it is open-source (and therefore very customizable), is designed for academic use and integrates well with LaTeX. As I read, I highlight some passages and make notes.

After I finish reading the paper, I have a PDF with a bunch of annotations. One of the nice features of Skim is that it saves them in a separate file, which is indexed by Spotlight and thus searchable. 

On the other hand, I have a folder (`~/Dropbox/notes`) full of notes files written in Markdown format. I have a note documenting how I set up a new Mac (or a new Windows machine); notes describing many key commands I've learned in Emacs; several notes about topics I've learned from many general non-fiction books. I am a compulsive note-taker. My notes directory is my [zettelkasten](http://zettelkasten.de )
, my central hub for ideas, my stored memory, my main reference. Any time I have a question, I search in this archive for answers. 

Now, how nice would it be to somehow store the *notes* from my PDF files in my *notes* archive?  Notes I've taken while reading a paper or thesis are just another type of information I want to store. So, taking advantage of Skim's scripting abilities, I created [`skim2md`](https://github.com/fabiofortkamp/skim2md ).

`skim2md` is an AppleScript that grabs all your notes and highlights from a Skim document and creates a Markdown file, with one paragraph per note. Each paragraph is preceded by a line stating which line this note was taken from.

Skim already has an "Export" function, but this script automates the process, placing the output file in the directory I want and with the formatting adjusted to my needs. With the Markdown file, it is easy to easily search for particular information, copy a quote or just intereact with other text files. In other words, a summary of an important document I read is then stored in my digital brain; if I want to investigate something with more detail, I open the PDF document and search for the relevant page.

I won't get into more details because you can go the [Github page](https://github.com/fabiofortkamp/skim2md ) 
 and there the information will always be up to date. If you already use Skim and have this need, or if you usually read PDFs, annotate them and would like a way to create a more lightweight, text-only version of your notes, give Skim and `skim2d` a try!

