"""EJ5
PIDE LA NOTA FINAL DE UN ESTUDIANTE DE 0 A 100, SI EL PROMEDIO ES MENOR IGUAL A 50 MOSTRAR REPROBADO CON LA NOTA DE REPROBACION 
Y SI ES MAYOR IGUAL A 51 MOSTRAR APROBADO CON LA NOTA DE APROBACION"""

nota = int(input("Escriba su nota: "))

while nota < 0 or nota >100:
    print ("Nota invalida")
    nota = int(input("Escriba su nota: "))

if nota >= 51:
    print ("Aprobado con la nota de aprobacion :D")
else:
    print (":(")