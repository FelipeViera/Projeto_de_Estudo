sequencia1 = ""
virgula1 = false
sequencia2 = ""
virgula2 = false
operador = ""


function calcular(){
    var entrada = document.getElementsByClassName("caixa")[0]

    //Vai pegar o valor  dos duas sequências e realizar o cálculo

    //Estes blocos condicionais servem para conferir qual cálculo deve-se fazer com base no operador
    if (sequencia2 != ""){
        if(operador == "+"){
            sequencia1 = Number.parseFloat(sequencia1) + Number.parseFloat(sequencia2)
            sequencia2 = ""
            operador = ""
        }

        else {
            if (operador == "-"){
                sequencia1 = Number.parseFloat(sequencia1) - Number.parseFloat(sequencia2)
                sequencia2 = ""
                operador = ""

            }

            else {
                if(operador == "x"){
                    sequencia1 = Number.parseFloat(sequencia1) * Number.parseFloat(sequencia2)
                    sequencia2 = ""
                    operador = ""
                }

                else {
                    if (operador == "/"){
                        sequencia1 = Number.parseFloat(sequencia1) / Number.parseFloat(sequencia2)
                        sequencia2 = ""
                        operador = ""
                    }
                }
            }
        }
        

        //Verifica se a sequência 1 tem ou não vírgula
        if (parseInt(sequencia1) != parseFloat(sequencia1)){
            virgula1 = true

        }

        
        virgula2 = false
        entrada.innerText = sequencia1 + operador + sequencia2
    }
    
}

function concatenar(valor){
    
    //Ele recebe o valor do botão e adiciona a sequência desejada
    var entrada = document.getElementsByClassName("caixa")[0]


    if (entrada.value == ""){
        sequencia1 = valor
        
    }

    else{
        if (operador == ""){
            sequencia1 += valor
        }
        else {
            if (sequencia2 != ""){
                sequencia2 += valor 
            }
            else {
                sequencia2 = valor
            }
        }
         
    }

    entrada.innerText = sequencia1 + operador + sequencia2
        

}





function operation(valor){

    if (sequencia1 != ""){
        operador = valor
    }
    //Adiciona um operador ao cálculo
    var entrada = document.getElementsByClassName("caixa")[0]
   

    entrada.innerText = sequencia1 + operador + sequencia2



}

function virgula(){
    //Lógica para colocar vírgula
    var entrada = document.getElementsByClassName("caixa")[0]
   if (sequencia1 == ""){
     sequencia1 = "0."
     virgula1 = true
   }
   else {
      if (operador == ""){
        if (virgula1 == false){
            sequencia1 += "."
            virgula1 = true
        }
      }
      else {
        if (sequencia2 == ""){
            sequencia2 = "0."
            virgula2 = true
        }
        else {
            if (virgula2 == false){
                sequencia2 += "."
                virgula2 = true
            }
        }
      }
   }

   entrada.innerText = sequencia1 + operador + sequencia2 
}


function deletar(){
    //Deleta tudo
    var entrada = document.getElementsByClassName("caixa")[0]
    operador = ""
    sequencia1 = ""
    sequencia2 = ""
    entrada.innerText = sequencia1 + operador + sequencia2

    
}

function subtrair(){
    //Deleta o último número
    var entrada = document.getElementsByClassName("caixa")[0]
    if (sequencia1 != ""){

        if (operador == ""){

            if (sequencia1.slice(-1) == "."){
                virgula1 = false
            }

            sequencia1 = sequencia1.slice(0, -1)
        }

        else {
            
            if (sequencia2 == ""){
                operador == ""
            }


            else {
                if (sequencia2.slice(-1) == "."){
                    virgula2 = false
                }
                sequencia2 = sequencia2.slice(0, -1)
            }
           
        }

        entrada.innerText = sequencia1 + operador + sequencia2

    }

}