<?php

function nextline()
{
  $file = new SplFileObject("lastserved.txt") ;
  $current = $file->current() ;
  $file = null ;
  $longfile = new SplFileObject("o1.txt") ;
  while(0 != strcmp(trim($longfile->current()), trim($current)))
  {
    $longfile->next() ;
  }
  $longfile->next() ;
  $newtop = $longfile->current() ;
  $longfile = null ;
  file_put_contents("lastserved.txt", $newtop) ;
  return trim($newtop) ;
}

$show = nextline() ;
echo '<html><META HTTP-EQUIV="REFRESH" CONTENT="45"><title>Ocean 1 Global Sequential Viewer</title><br>' ;
echo "<a target='_blank' href='https://tucc.us/noted.php?fname=" ;
echo $show ;
echo "'>Click here if this picture stands out, even just a part of it.</a><br>" ;
echo "<img width='60%' src='http://b0ps.s3-us-west-2.amazonaws.com/ocean1/" ;
echo $show ;
echo "'>" ;
echo '</body></html>' ;
?>

