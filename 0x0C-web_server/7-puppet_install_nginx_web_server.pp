#!/usr/bin/env bash
#installs Nginx, configures it to respont to a GET request with "Hello World!" and carries out a permanent redirection

package { 'nginx':
    ensure  => installed,
}

exec { 'configure nginx':
    path    => '/usr/bin',
    command => "echo 'Hello World!' | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i \"s/^[^#].*server_name.*/server_name _;\nrewrite ^/redirect_me / permanent;/\" /etc/nginx/sites-available/default ; sudo service nginx start;",
}
