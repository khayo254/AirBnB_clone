#!/bin/bash
# Check if Nginx is installed, install it if not found
if ! command -v nginx >/dev/null 2>&1; then
    sudo apt-get update && sudo apt-get install -y nginx
fi

# Ensure necessary directories exist
ensure_directory_exists() {
    local directory=$1
    if [[ ! -d "$directory" ]]; then
        mkdir -p "$directory"
    fi
}

ensure_directory_exists "/data"
ensure_directory_exists "/data/web_static"
ensure_directory_exists "/data/web_static/releases"
ensure_directory_exists "/data/web_static/shared"
ensure_directory_exists "/data/web_static/releases/test"

# Create a dummy HTML file in the test directory
echo "<html><body>Hello World!</body></html>" > /data/web_static/releases/test/index.html

# Create a symbolic link to the current release directory
if [[ -L "/data/web_static/current" ]]; then
    rm -f "/data/web_static/current"
fi
ln -s "/data/web_static/releases/test" "/data/web_static/current"

# Assign ownership of the data directory to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data

# Update Nginx configuration to serve content from /data/web_static/current/ to hbnb_static
sudo sed -i 's|server {|server {\n\tlisten 80;\n\tserver_name mydomainname.tech;\n\troot /data/web_static/current;\n}|g' /etc/nginx/sites-available/default

# Restart Nginx service
sudo service nginx restart