#This script installs and configures Nginx to return a custome header

exec { 'update packages, install nginx':
    path    => '/usr/bin',
    command => 'sudo apt-get -y update; sudo apt-get -y install nginx',
}

exec { 'add header':
    path    => '/usr/bin',
    command => 'sudo sed -i \'s|^[^#].*try_files ${uri} ${uri}/ =404;|\t\ttry_files ${uri} ${uri}/ =404;\n\t\tadd_header X-Served-By ${hostname};|\' /etc/nginx/sites-available/default',
}

exec {'restart/start nginx':
    path    => '/usr/bin',
    command => 'sudo service nginx restart',
}
