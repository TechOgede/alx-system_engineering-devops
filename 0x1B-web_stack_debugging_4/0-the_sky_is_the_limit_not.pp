#Raise the Nginx file limit to 4096

exec { 'raise limit':
    provider => shell,
    command  => 'sudo sed -i "s|-n 15|-n 4096|" /etc/default/nginx',
    before   => Exec['restart'],
}

exec { 'restart':
    provider => shell,
    command  => 'sudo service nginx restart',
}
