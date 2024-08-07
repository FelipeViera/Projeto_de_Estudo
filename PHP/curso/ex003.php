<?php

class Computador {
    public $cpu;
    function ligar(){
        echo "Ligando o computador a {$this->cpu}...";
    }
}

$objeto = new Computador;
$objeto->cpu = "450Mz";
$objeto->ligar();

?>