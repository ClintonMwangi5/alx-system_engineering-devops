# This Puppet manifest fixes a missing permissions issue for the Apache document root

exec { 'fix-apache-permissions':
  command => '/bin/chmod -R 755 /var/www/html',
  onlyif  => '/usr/bin/find /var/www/html -not -perm 755',
}

service { 'apache2':
  ensure => running,
  enable => true,
  subscribe => Exec['fix-apache-permissions'],
}
