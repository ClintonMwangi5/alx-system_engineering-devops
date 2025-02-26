# 0-strace_is_your_friend.pp
# This Puppet manifest fixes the issue causing Apache to return a 500 error.

# Ensure the parent directory exists
file { '/var/www/html/wp-content':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Ensure the uploads directory exists
file { '/var/www/html/wp-content/uploads':
  ensure => 'directory',
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Ensure the correct permissions for the WordPress files
exec { 'fix-wordpress':
  command => 'chown -R www-data:www-data /var/www/html/*',
  path    => '/usr/bin',
  onlyif  => 'test ! -w /var/www/html',
}
