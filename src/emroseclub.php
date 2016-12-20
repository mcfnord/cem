<?php
$file="empix.txt";
$linecount = 0;
$handle = fopen($file, "r");
while(!feof($handle)){
  $line = fgets($handle);
  $linecount++;
}

fclose($handle);

# echo $linecount;

$which = rand ( 0, $linecount - 1 );
$file = new SplFileObject($file);
$file->seek( $which );
echo '<html><META HTTP-EQUIV="REFRESH" CONTENT="45"><title>Emily Rose Club</title><body bgcolor=black><center><font size="+2"><br></font>' ;

echo '<br><font color="white"><i><b><a href="/">another</a></b></i><br>' ;	

if (isset($_GET['my']))  // the my param is our source
{ 
	echo "<img width='80%' src='" ;
	echo urldecode( $_GET['my'] ) ; 
	echo "'>" ;
} 
else
{
	echo $file->current() ; // read it from the file
}

$file="link_list.txt";
$linecount = 0;
$handle = fopen($file, "r");
while(!feof($handle)){
  $line = fgets($handle);
  $linecount++;
}

# flip a coin heads twice to see something I can read.
$show = rand ( 0, 3 ); 
if( 0 == $show )
	{
	$which = rand ( 0, $linecount - 1 );
	$file = new SplFileObject($file);
	$file->seek( $which );

	echo "<br><b><a target='blank' href='" ;
	echo rtrim($file->current()) ;
	echo "'>Read...</a></b>" ;
	}

echo '</center></font></body>' ;	
?>
