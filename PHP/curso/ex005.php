<?php 


echo Ola("Kleber", "Juliano", "Oswald");


function Ola(){
    $argumentos = func_get_args();
    $quantidade = func_num_args();
    for ($i = 0; $i < $quantidade; $i++){
        echo $argumentos[$i], "<br>";
    }
}


?>
