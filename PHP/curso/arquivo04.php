<?php 

$original = "file.txt";
$copia = "copia_fille.txt";

if (copy($original, $copia)){
    echo "copia efetuada";
}
else{
    echo "erro ao efetuar a cópia";
}

?>