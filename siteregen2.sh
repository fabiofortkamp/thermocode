#!/bin/bash
# source: http://www.macdrifter.com/2013/05/the-road-to-pelican-32.html
export LANG=en_US.UTF-8

cd /home/fabiofortkamp/sites/thermocode.net
source activate blog

### Kick that Pelican into action by pointing it at the config file and log the output
/home/fabiofortkamp/miniconda3/envs/blog/bin/pelican -s /home/fabiofortkamp/sites/thermocode.net/publishconf.py >> /home/fabiofortkamp/thermocode.net.cron.log 2>&1
### Timestamp that bad boy.
echo "siteregen2.sh: $(date)" >> /home/fabiofortkamp/thermocode.net.cron.log 2>&1
