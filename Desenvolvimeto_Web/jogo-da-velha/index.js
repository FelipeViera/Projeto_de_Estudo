var player = 0 
var listap1 = []
var listap2 = []


function Reiniciar(){
    location.reload()
}

function Escolha(id){
    var x = document.getElementById('x')
    var o = document.getElementById('o')



    if (listap1.length == 0 && listap2.length == 0){
        //alert('sim')
        if ( id == "x"){
            player = 0
            x.style.backgroundColor = "rgb(166, 96, 232)"
            o.style.backgroundColor = "white"
            
        }
        else {
            player = 1
            o.style.backgroundColor = "rgb(166, 96, 232)"
            x.style.backgroundColor = "white"
        }
    }
}

function Clique(valor){
    var entrada = document.getElementById(valor)

    if (entrada.innerText != "X" && entrada.innerText != "O"){

        if (player == 0){
            entrada.innerText = "X"
            player = 1
            listap1.push(valor)
            var jogador = listap1

        }

        else {
            if (player < 3){
                entrada.innerText = "O"
                player = 0
                listap2.push(valor)
                var jogador = listap2
            }
            
        }
        return verificar(jogador)
    }
}


function verificar(jogador){

    if (jogador.length >= 3){

        //Vitórias horizontais

        if (jogador.includes('cl1-ln1') && jogador.includes('cl2-ln1') && jogador.includes('cl3-ln1')) {
            player = 3

            lista = ['cl1-ln1', 'cl2-ln1', 'cl3-ln1']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }
        
            
            

        }

        if (jogador.includes('cl1-ln2') && jogador.includes('cl2-ln2') && jogador.includes('cl3-ln2')) {
           
            player = 3

            lista = ['cl1-ln2', 'cl2-ln2', 'cl3-ln2']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }

        }

        if (jogador.includes('cl1-ln3') && jogador.includes('cl2-ln3') && jogador.includes('cl3-ln3')) {
            

            player = 3

            lista = ['cl1-ln3', 'cl2-ln3', 'cl3-ln3']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }
        }



        //Vitórias verticais 

        if (jogador.includes('cl1-ln1') && jogador.includes('cl1-ln2') && jogador.includes('cl1-ln3')) {
            lista = ['cl1-ln1', 'cl1-ln2', 'cl1-ln3']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }

            player = 3
        }

        if (jogador.includes('cl2-ln1') && jogador.includes('cl2-ln2') && jogador.includes('cl2-ln3')) {
            lista = ['cl2-ln1', 'cl2-ln2', 'cl2-ln3']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }
            player = 3
        }

        if (jogador.includes('cl3-ln1') && jogador.includes('cl3-ln2') && jogador.includes('cl3-ln3')) {
            lista = ['cl3-ln1', 'cl3-ln2', 'cl3-ln3']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }
            player = 3
        }

        //Vitórias diagonais

        if (jogador.includes('cl1-ln1') && jogador.includes('cl2-ln2') && jogador.includes('cl3-ln3')) {
            lista = ['cl1-ln1', 'cl2-ln2', 'cl3-ln3']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }
            player = 3
        }

        if (jogador.includes('cl3-ln1') && jogador.includes('cl2-ln2') && jogador.includes('cl1-ln3')) {
            lista = ['cl3-ln1', 'cl2-ln2', 'cl1-ln3']

            for (i = 0; i < lista.length; i++){
                var entrada = document.getElementById(lista[i])
                entrada.style.backgroundColor = "rgb(41, 229, 41)"
            }
            player = 4
        }

    }

}