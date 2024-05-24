sequencia1 = ""
virgula1 = false
virgula2 = false
sequencia2 = ""
operador = ""


function calcular(){
    var entrada = document.getElementsByClassName("caixa")[0]

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
        
        virgula2 = false
        entrada.innerText = sequencia1 + operador + sequencia2
    }
    
}

function concatenar(valor){
    
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
   
    var entrada = document.getElementsByClassName("caixa")[0]
    operador = valor

    entrada.innerText = sequencia1 + operador + sequencia2



}

function virgula(){
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

    var entrada = document.getElementsByClassName("caixa")[0]
    operador = ""
    sequencia1 = ""
    sequencia2 = ""
    entrada.innerText = sequencia1 + operador + sequencia2

    
}

function subtrair(){
    //Adicionar funcionalidade de remover o último número 
}