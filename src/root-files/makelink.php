<?php
# call this from makelink.bat, which is in the path for this PC

if(false === isset($_GET['cute']))
  { echo 'ERROR' ; return ; }

if(false === isset($_GET['ugly']))
  { echo 'ERROR' ; return ; }

$local_dir = $_GET['cute'] ;

if(file_exists ( $local_dir ))  //  does dest exist on this server?
  { echo 'ERROR' ;   return ; } // does exist? then fail.
else
  {
  echo $local_dir ;

  echo mkdir( './_/' . $local_dir, 0777, true ) ;   # recursive ok

  // and put the dest url redirector in it in its simplest form.
  $payload = "<HTML><HEAD><META HTTP-EQUIV='REFRESH' CONTENT='1;URL=" . $_GET['ugly'] . "'></HEAD></HTML>" ;

  // create a default index.php file in that dir
  $index_script = $local_dir . "/_/index.php" ;
  file_put_contents($index_script, $payload);

  // and return the popular url
  echo 'http://em-is.us/_/' . $local_dir ;
  return ;
}
?>
