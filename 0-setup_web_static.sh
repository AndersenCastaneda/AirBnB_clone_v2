#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static
apt-get -y update
apt-get install -y nginx
ufw allow "Nginx HTTP"
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/server_name _;/ a \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t} " /etc/nginx/sites-enabled/default
service nginx restart
