<?php 

$notas = array(5, 2, 5, 3.5);

echo media_calculo($notas);

function media_calculo($notas){
    $nota_total = 0;
    for ($i = 0; $i < 4; $i++){
        $nota_total += $notas[$i];
    }
    return $nota_total/5;
}

?>