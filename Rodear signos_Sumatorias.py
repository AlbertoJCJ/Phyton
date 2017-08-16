"****************************NUMERO1*************************************************************"
def rodearPalabra():
    palabra=input("Introduzca una palabra")
    simbolo=input("Introduzca un simbolo")

    print ("\n",simbolo,simbolo,simbolo,simbolo,simbolo,simbolo,simbolo,"\n",
           simbolo,simbolo,palabra,simbolo,simbolo,"\n",
           simbolo,simbolo,simbolo,simbolo,simbolo,simbolo,simbolo)

    return rodearPalabra()


"***************************NUMERO 2****************************************************************"
def pSimilitud():

    contador=0
    lista1 = []

    palabra1 = input("Inserte la primera palabra: ")
    palabra2 = input("Inserte la Segunda palabra: ")

    for i in palabra1:
      lista1.append(i)

    for j in palabra2:
      lista1.append(j)

    for i in lista1:


     if i == j :
      contador+=1




     if len(palabra1) > len(palabra2):
            longitudes = palabra1



     elif len(palabra2) > len(palabra1):
          longitudes = palabra2




     else : longitudes=palabra1


     porcentaje =(contador * 100)/longitudes
     print(porcentaje)

    return pSimilitud()

"***********************************NUMERO3*****************************************************"
def multiplicacionSumatorias():

    inicio=int(input("Introduzca un inicio: "))
    final=int(input("Introduzca el final: "))
    factor=int(input("Introduzca el factor: "))

    contador = inicio
    resultado=0+1


    while contador<=final:
         if contador %factor==0:
            resultado*=contador

         print(resultado,contador)

         contador+=1

    return multiplicacionSumatorias()




"******************************************MENU INICIO************************************************************"
def MenuInicio ():
    print(" MENU INICIO","\n1)""RODEAR PALABRA","\n2)""PORCENTAJE PALABRA","\n3)""MULTIPLICAION DE SUMATORIA")


    inicio=int(input())

    if inicio == 1:
        print("Rodear Palabra")
        resultado=rodearPalabra()
        print(resultado)



    elif inicio==2:
         print("Similitud en palabras")
         resultado=pSimilitud()
         print(resultado)


    elif inicio==3:
        print("Multiplicación de Sumatoria")
        resultado=multiplicacionSumatorias()
        print(resultado)
        return MenuInicio()
MenuInicio()