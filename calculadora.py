num1 = 0
num2 = 0

while True:

    print("Bienvenido a nuestro proyecto de calculadora ")
    print("1- Desea Sumar")
    print("2- Desea Restar")
    print("3- Desea Multiplicar")
    print("4- Desea dividir")
    print("5- Desea salir")
    print("Porfavor seleccione un numero del (1-5)")
    opc = int(input())


    if opc == 1:
        num1 = int(input("Porfavor digame su numero a sumar: "))
        num2 = int(input("Porfavor deme el segundo numero a sumar: "))
        resultado = num1 + num2
        print(f"La suma de sus numero da como resultado { resultado }")
    
    elif opc == 2:
        num1 = int(input("Porfavor digame su numero a restar: "))
        num2 = int(input("Porfavor deme el segundo numero a restar: "))
        resultado = num1 - num2
        print(f"La resta de sus numero da como resultado { resultado }")

    elif opc == 3:
        num1 = int(input("Porfavor digame su numero a multiplicar: "))
        num2 = int(input("Porfavor deme el segundo numero a multiplicar: "))
        resultado = num1 * num2
        print(f"La multiplicacion de sus numero da como resultado { resultado }")

    elif opc == 4:
        num1 = float(input("Porfavor digame su numero a dividir: "))
        num2 = float(input("Porfavor deme el segundo numero a dividir: "))
        resultado = num1 / num2
        print(f"La division de sus numero da como resultado { resultado }")

    elif opc == 5:
        print("Usted esta saliendo de la calculadora")
        break
    else:
        print("Error")


        

