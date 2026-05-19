#numero_escolhido
#operação escolhida
#segundo numero escolhido
#usuario clica =
#faz calculo
#joga pra tela

import math


numero_escolhido1 = ""
operação = None
numero_escolhido2 = ""



def adicionar_numero(numero):
    global numero_escolhido1,numero_escolhido2,operação

    if operação is None:
        numero_escolhido1 += str(numero)
        
        return numero_escolhido1
    
    
    else:
        numero_escolhido2 += str(numero)
        
        return numero_escolhido2
    

    
    
    
    
    

    


def def_operação(op):
    global operação
    operação = op
    



def calcular():
    global numero_escolhido1,numero_escolhido2,operação
    num1 = float(numero_escolhido1)
    

    if operação == "²√x":
        resultado = math.sqrt(num1) 
        return f"{resultado:.1f}"
    
    if operação == "x²":
        return num1 ** 2
    
    num2 = float(numero_escolhido2)

    if operação == "+":
        resultado = num1 + num2 
        return f"{resultado:.1f}"

    elif operação == "-":
        resultado = num1 - num2 
        return f"{resultado:.1f}"
    
    elif operação == "x":
        resultado = num1 * num2
        return f"{resultado:.1f}"
    
    elif operação == "/":
        resultado = num1 / num2
        return f"{resultado:.2f}"
    
    
    
    
    
    

def limpar_tela():
    global numero_escolhido1,numero_escolhido2,operação
    numero_escolhido1 = ""
    numero_escolhido2 = ""
    operação = None

    return "0"

     
    






