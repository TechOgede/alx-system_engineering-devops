# Executes a command to kill a process named 'killmenow'

exec { 'pkill killmenow':
    path   => '/usr/bin',
}
