# Fix errorneous line in Wordpress setting file to resolve the 500 error

exec {'fix file extension':
    provider => shell,
    command  => 'sudo sed -i "s/\.phpp/.php" /var/www/html/wp-settings.php'
}
