<?php
# call this from makelink.bat, which is in the path for this PC

if(false === isset($_GET['cute_url']))
	{
	echo 'ERROR' ;
	return ;
	}

if(false === isset($_GET['ugly_url']))
	{
	echo 'ERROR' ;
	return ;
	}

$local_dir = $_GET['cute_url'] ;

if(file_exists ( $local_dir ))  # does dest exist on this server?
	{
		echo 'ERROR' ;    # it exists, and that's an error!
		return ;
	}
	else
	{
		mkdir( $local_dir ) ;   # dir doesn't exist so we make it

		# and put the dest url redirector in it in its simplest form.
		$payload = "<HTML><HEAD><META HTTP-EQUIV='REFRESH' CONTENT='1;URL=" . $_GET['ugly_url'] . "'></HEAD></HTML>" ;

		#create a default index.php file in that dir
		$index_script = $local_dir . "/index.php" ;
		file_put_contents($index_script, $payload);
		
		# and return the popular url
		echo 'http://em-is.us/' . $local_dir ;
		return ;
	}
?>
