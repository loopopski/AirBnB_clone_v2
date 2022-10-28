#!/usr/bin/env bash
# set up dummy html

server="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-available/default"
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir "/data/web_static/shared/"
echo "Holberton" > "/data/web_static/releases/test/index.html"
rm -f "/data/web_static/current"; ln -s "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -hR ubuntu:ubuntu "/data/"
sudo sed -i "29i\ $server" "$file"
sudo service nginx restart
