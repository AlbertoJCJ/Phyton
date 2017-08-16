"***********************PAGINA 94 NUMERO 1***************************"
def exclusion():
    numero=int(input("Inserte un numero entre 0 y 10"))

    if numero < 0 and numero > 10:
        print("Número invalido pruebe con otro numero.")
        return exclusion()
    else:print(numero)
    exclusion()
exclusion()
"**************************NUMEROS MAYOR Y NUMER MENOR********************************************"
listanum=[]

def contadorMenores():

    numero=int(input("Inserte un numero: "))

    if numero > 0:
        listanum.append(numero)
        print(listanum)
    else:
        print(numero,"Es negativo")
        print(listanum)
        print("EL NUMERO MAYOR ES: ",max(listanum),"\n""EL NUMERO MENOR ES: ", min(listanum),"\n""ADIOS")

    contadorMenores()
contadorMenores()
"*********************************************MULTIPLOS DE 6********************************************************************"
def multiplosDe6():
    numero=6
    contador=0
    while contador <= 150:
          if contador < 150:
              numero+=6
              contador+=6
              print(contador)
multiplosDe6()
"***********************************************************************************************************************"

