#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install nginx if it not already installed
if [ ! -x /usr/sbin/nginx ]; then
    sudo apt-get -y install nginx
fi

# Create the folders
mkdir -p /data/web_static/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create a fake HTML file
string_index="<html><head></head><body>Holberton School</body></html>"
echo "$string_index" > /data/web_static/releases/test/index.html

# Create a symbolic link 
# (deleted and recreated every time the script is ran)
ln -sf  /data/web_static/releases/test/ /data/web_static/current

# change group and user
# link: https://linuxize.com/post/linux-chown-command/
chown -R ubuntu:ubuntu /data/

#
new_string="location /hbnb_static {alias /data/web_static/current/;}"
string_to_replace="listen 80 default_server;"
sed -i "/$string_to_replace/ a $new_string" /etc/nginx/sites-enabled/default
sudo service nginx restart
