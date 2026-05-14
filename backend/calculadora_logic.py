#numero_escolhido
#operação escolhida
#segundo numero escolhido
#usuario clica =
#faz calculo
#joga pra tela


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
    num2 = float(numero_escolhido2)

    if operação == "+":
        return  num1 + num2 

    elif operação == "-":
        return num1 - num2 
    
    
def zerar_calculo():
    global numero_escolhido1,numero_escolhido2
    numero_escolhido1 = ""   
    numero_escolhido2 = ""         
    






