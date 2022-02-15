<?php

$fp = fopen('noted.txt', 'a') ;
fwrite($fp, $_GET['fname']) ;
fwrite($fp, "\r\n" ) ;
fclose($fp) ;
echo '<html><body>Thanks! Flag more pictures!</body></html>' ;

?>
