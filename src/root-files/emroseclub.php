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
try_again:
  $which = rand ( 0, numlines($filename) - 1 );
  $file = new SplFileObject($filename);
  $file->seek( $which );
  $line = $file->current() ; // read it from the file
  if( strlen($line) < 4)     // filename plus extension plus dot is probably longer!
     goto try_again;
  echo $line ;
}

echo '<html><META HTTP-EQUIV="REFRESH" CONTENT="45"><title>Emily Rose Club</title><body bgcolor=black><center><font size="+2"><br></font>' ;

if( 0 == rand( 0, 3 ))
{
  echo "<br><audio autoplay><source src='" ;
  echo randoline("trax.txt") ;
  echo "'></audio>" ;
}

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

echo '</center></font></body></html>' ;
?>
