"""EJ4
PIDE UN NUMERO ENTERO AL USUARIO E INDICA MEDIANTE UN MENSAJE
SI EL NUMERO INGRESADO EN PAR O IMPAR"""

num = int(input("Ingrese su numero: "))

if num % 2 == 0:
    print ("Su numero es par")
else:
    print ("Su numero es impar")