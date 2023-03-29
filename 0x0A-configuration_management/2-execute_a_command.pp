# Create a manifest file that kills a process
exec { 'kill process':
  command  => 'pkill killmenow',
  provider => 'shell',
}
