<?php 
//Coloca cada linha do arquivo em um vetor
$arquivo = file ("file.txt");

for ($i = 0; $i < 3; $i++){
    echo $arquivo[$i], "<br>";
}

?>