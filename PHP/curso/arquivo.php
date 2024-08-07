<?php 

$fd = fopen("file.txt", "r");
while (!feof($fd)){

    $buffer = fgets($fd, 4096);
    echo $buffer;
}

fclose($fd);

?>