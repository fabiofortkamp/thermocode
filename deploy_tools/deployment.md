# Deploying thermocode.net

**thermocode.net** is a site built with [pelican](http://docs.getpelican.com/en/3.6.3/). The main folder consists of a settings file (`pelicanconf.py`) and a `content` folder, with some auxiliary files.

There is a [repository](https://github.com/fabiofortkamp/thermocode) with all the necessary files, *except* the content folder. This folder should be symlinked to the main folder, otherwise the site will not be built!

To deploy the site to a server (running Ubuntu), log in to the server and create a folder `~/sites/` and clone the repository (`SITENAME` is the domain that will be used)

	git clone --recursive https://github.com/fabiofortkamp/thermocode SITENAME

Create the `content` folder or symlink from Dropbox.

	ln -s ~/Dropbox/thermocode-posts ~/sites/SITENAME/content

Inside the main folder, with miniconda installed, create the environment:

	conda env create

Activate the environment:

	source activate thermocode

And try to build, just to test the environment

	pelican

If no error messages, create the public directory where the html will reside and symlink the output folder:

	sudo mkdir -p /var/www/SITENAME/public_html
	sudo mkdir -p /var/www/SITENAME/logs
	sudo ln -s ~/sites/SITENAME/output /var/www/SITENAME/public_html

Now, start to replace the SITENAME variable.

Create a template for nginx:

	sed "s/SITENAME/thermocode.net/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/thermocode.net

Create a symlink for the `enabled` sites:

	sudo ln -s /etc/nginx/sites-available/thermocode.net /etc/nginx/sites-enabled/

Install the publishing settings:

	sed "s/SITENAME/thermocode.net/g" deploy_tools/publishconf.py | tee /home/fabiofortkamp/sites/thermocode.net/publishconf.py

Create a `~/bin` directory:

	mkdir -p ~/bin

Install the site generation script:

	sed "s/SITENAME/thermocode.net/g" deploy_tools/siteregen2.sh | tee /home/fabiofortkamp/bin/thermocode.net.siteregen2.sh

Create a new cron job:

	crontab -e

And add the following line:

	*/5 * * * * sh ~/bin/thermocode.net-siteregen2.sh

Finally, reload nginx:

	sudo service nginx reload

If there is any error, debug with:

	sudo nginx -t
