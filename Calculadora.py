def sumadora(num1,num2):
    suma=num1+num2
    return suma()


def restadora (num1,num2):
    num1>num2
    resta =num1-num2
    return resta()

def multiplicaciones(num1,num2):
    multiplicacion=num1*num2
    return multiplicacion()

def divisiones (num1,num2):
    num1>num2
    division=num1/num2
    return division()

def conversorCD():
    monto=int(input("Inserte monto en colones"))
    colonD=monto/554.65
    print(colonD)
    return colonD

def conversorDolarC():
    monto=int(input("Inserte monto en dolares "))
    dolarC=monto*554.65
    print(dolarC)
    return dolarC
def conversorcolonE():
    monto = int(input("Inserte monto en colones "))
    colonE=monto/589.238
    print(colonE)
    return colonE
def conversoreuroC():
    monto = int(input("Inserte monto en euros "))
    euroC=monto*589.238
    print(euroC)
    return euroC
def conversorcolonY():
    monto = int(input("Inserte monto en colones "))
    colonY=monto/0.206
    print(colonY)
    return colonY
def conversorYenC():
    monto = int(input("Inserte monto en Yenes "))
    yen=monto*4.865
    print(yen)
    return yen

print("Digite su nombre: ")
print("Hola", input())
print("¿Que desea realizar?")





herramienta=print("\n1)Calculadora""\n2)Nota Curso")
seleccionProceso=input()
print("¿Que proceso desea realizar?")







if seleccionProceso== "1":




  def calculadora ():
    print("CALCULADORA")
    print("\n1)SUMA""\n2)RESTA""\n3)MULTIPLICACION""\n4)DIVISION""\n5)IMC""\n6)CONVERSOR")
    opcion = input()

    if opcion == "1":
        print("*****SUMA*****")
        num1=int(input("Inserte el primer número: "))
        num2=int(input("Inserte el segundo número: "))
        resultado=num1+num2
        print("El resultado de la suma es: "+str(resultado))
        return calculadora()

    if opcion=="2":
       print("RESTA")
       num1 = int(input("Inserte el primer número: "))
       num2 = int(input("Inserte el segundo número: "))
       resultado = num1 - num2
       print("El resultado de la resta es: "+str(resultado))
       return calculadora()
    if opcion=="3":
        print("MULTIPLICACION")
        num1 = int(input("Inserte el primer número: "))
        num2 = int(input("Inserte el segundo número: "))
        resultado = num1 * num2
        print("El resultado de la multiplicacion es: " + str(resultado))
        return calculadora()
    if opcion=="4":
        print("DIVISION")
        num1 = int(input("Inserte el primer número: "))
        num2 = int(input("Inserte el segundo número: "))
        resultado = num1 / num2
        print("El resultado de la division es: " + str(resultado))
        return calculadora()
    if opcion == "5":



       print("Calculador IMC")
       Altura = float(input("Inserte su altura: "))
       Peso = float(input("Inserte su peso: "))
       imc =Peso/(Altura*Altura)

       if imc <= 18:
           print(imc,(" Peso bajo. Necesario valorar signos de desnutrición"))

       if imc>=18 and imc<=24.99995:
           print (imc, ("Normal"))

       if imc>=25 and imc <=26.9:
           print(imc, ("Sobrepeso"))
       if imc > 27:
           print(imc,("Obesidad"))
       if imc >=27 and imc <=29.9:
           print(imc,("Obesidad grado 1.  Riesgo relativo alto para desarrollar enfermedades cardiovasculares"))
       if imc >=30 and imc <=39.9:
           print(imc,("Obesidad grado II. Riesgo relativo muy alto para el desarrollo de enfermedades cardiovasculares"))
       if imc >= 40:
           print(imc,("Obesidad grado III Extrema o Mórbida. Riesgo relativo extremadamente alto para el desarrollo de enfermedades cardiovasculares"))
       return calculadora()



    if opcion=="6":
          print("Conversor de moneda")
          print("Que clase de conversion quiere hacer:""\n1)Colón a Dolar""\n2)Dolar a Colon""\n3)Colon a Euro""\n4)Euro a Colon"
                "\n5)Colon a Yen""\n6)Yen a Colon""\n7)Colon a Libra Esterlina""\n8)Libra Esterlina a Colon")
          eleccion=int(input())
          if eleccion == 1:
             print("CONVERSOR DE COLON A DOLAR")
             resultado=conversorCD()
             print(resultado)





calculadora()


    