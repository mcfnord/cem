<?php

function numlines($filename)
{
  $linecount = 0;
  $handle = fopen($filename, "r");
  while(!feof($handle)){
    $line = fgets($handle);
    $linecount++;
  }
  fclose($handle);
  return $linecount;
}

function randoline($filename)
{
  $which = rand ( 0, numlines($filename) - 1 );
  $file = new SplFileObject($filename);
  $file->seek( $which );
  echo $file->current() ; // read it from the file
}

echo '<html><META HTTP-EQUIV="REFRESH" CONTENT="45"><title>Emily Rose Club</title><body bgcolor=black><center><font size="+2"><br></font>' ;
echo '<br><font color="white"><i><b><a href="/">another</a></b></i><br>' ;

if (isset($_GET['my']))   // the my param is our source
{
	echo "<img width='80%' src='" ;
	echo urldecode( $_GET['my'] ) ;
	echo "'>" ;
}
else
{
  echo randoline("empix.txt");
}

if( 0 == rand( 0, 3 ))    // flip a coin heads twice to see something I can read.
{
  echo "<br><b><a target='blank' href='" ;
  echo trim(randoline("link_list.txt")) ;
  echo "'>Read...</a></b>" ;
}

echo '</center></font></body>' ;
?>
