# thermocode

This is the repository **thermocode.net**, a blog created with [pelican](https://github.com/getpelican/pelican).

This setup assumes Python 3 and the [miniconda](http://conda.pydata.org/docs/) system. To create an environment with all necessary packages, type

	conda env create -f environment.yml

And then

	source activate thermocode

## The content folder

This repo is designed to be the basis for the blog infrastructure, so there is no `content` folder. I modify the site layout very rarely, but write posts often and from various platforms (OS X and iOS). Since there is not an easy way to use Git in iOS, I store my posts in a Dropbox folder, which is synchronized with the server. The site is then periodically rebuilt.

For this to work, one must create a `content` folder and symlink to this directory.
