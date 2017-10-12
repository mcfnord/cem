<?php

exec("tar -xf oceanv3.tar $_GET['f']");
$imagefile = 'http://tucc.us/o1/'.$_GET['f'];
$image=imagecreatefromgif($imagefile);
header('Content-type: image/gif'); #inadequate!

imagegif($image);
imagedestroy($image);
?>
