# Add private key to ssh_config file and modify file so that passwords arent supported

exec { 'modify /etc/ssh/ssh_config':
    path    => '/usr/bin/',
    command => "echo -e '#\tIdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config; sed -i 's/#*PasswordAuthentication yes/# PasswordAuthentication no/' /etc/ssh/ssh_config",
}
