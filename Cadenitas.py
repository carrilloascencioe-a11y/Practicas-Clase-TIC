Nombre="Erick" 
Frase="Sin acción, los sueños son solo palabras"
print(Nombre)
print(Frase)
#MOSTRAR EL NOMBRE EN MAYUSCULAS
print(Nombre.upper())
print(Frase.upper())
#MOSTRAR EL NOMBRE EN MINUSCULAS
print(Nombre.lower())
print(Frase.lower())
#OBTENER UN CARACTER EN UNA POSICION
letra=Frase[4]
print(letra)
#REALIZAR CORTE EN LA ORACION
Frase2="El-Mundo-es-Bonito"
print(Frase2.split("-"))
NombreC="Erick Zaid Carrillo Ascencio"
print(NombreC.split(" "))
#Dos primeras letras del nombre
letras1=NombreC[0:2]
print(letras1)
#REMPLAZAR EN LA CADENA
NuevaFrase=Frase.replace("sueños","Deseos")
print(NuevaFrase)
#NUMERO DE CARACTERES DE LA CADENA: LARGA
largoCadena=len(NuevaFrase)
print(largoCadena)