# puppet script to increase the amount of request nginx can handle

# Increase the ULIMIT of nginx
exec { 'Increase the limit':
  command => 'sed -i "s/15/4096" /ets/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restart my nginx
exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
