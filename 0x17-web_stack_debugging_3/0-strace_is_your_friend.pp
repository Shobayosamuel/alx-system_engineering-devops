# puppet script to authomate apache error

exec {'fix-line-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin','/usr/bin']
}
