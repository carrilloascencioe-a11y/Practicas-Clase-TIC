#CALIFICACIONES 
calif=float(input("Escribe tu Calificación"))
if calif==10:
    print("Exelente!!!")
elif calif==9:
    print("Muy Bien")
elif calif==8:
    print("Bien")
elif calif==7:
    print("Puedes Mejorar")
elif calif==6:
    print("Ay Mijooo :(")
elif calif==5:
    print("Chanclazoooo :(")
#TEMPERATURA
Temp=float(input("Escribe la Temperatura"))
if Temp>=40:
    print("Hace Mucho Calor")
elif Temp>=30 and Temp<40:
    print("Esta Templadito")
elif Temp>=20 and Temp<30:
    print("Esta Fresco")
elif Temp<=20:
    print("Hace Frio")
else:
    print("No Valida") 
#SEXO Y EDAD
Sexo=input("Ingresa tu Sexo ")
Edad=int(input("Ingresa tu Edad "))
if Sexo=="hombre" and Edad>=18:
    print("Puedes Sacar Cartilla Mailitar")
else:
    print("No Valido")