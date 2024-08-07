<?php 

$fp = fopen("file.txt", "w");

fwrite($fp, "linha 1\n");
fwrite($fp, "linha 2\n");
fwrite($fp, "linha 3\n");
?>