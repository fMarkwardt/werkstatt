# Nutze ein minimales Webserver-Image
FROM nginx:alpine

# Kopiere alle Dateien in den NGINX-Webserver-Ordner
COPY . /usr/share/nginx/html

# NGINX läuft automatisch auf Port 80
EXPOSE 80
