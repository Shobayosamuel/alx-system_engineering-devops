#!/bin/bash

# Use Puppet to automate the task of creating a custom HTTP header response

cat << EOF > /etc/puppetlabs/code/environments/production/manifests/init.pp
exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present',
  require => Exec['update'],
}

file { '/etc/nginx/nginx.conf':
  ensure => 'file',
  require => Package['nginx'],
}

file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"\${hostname}\";",
  require => File['/etc/nginx/nginx.conf'],
  notify => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File_line['http_header'],
}
EOF

# Run puppet apply
sudo /opt/puppetlabs/bin/puppet apply /etc/puppetlabs/code/environments/production/manifests/init.pp
