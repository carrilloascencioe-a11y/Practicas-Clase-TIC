Sexo=input("Ingresa tu Sexo ")
Edad=int(input("Ingresa tu edad "))
EstadoCivil=input("Ingresa tu Estado Civil ")
Hijos=int(input("Ingresa tu Cantidad de Hijos "))
if Sexo=="mujer" and Hijos==1 and Edad<18:
    print("Eres mujer, tienes un hijo y eres menor de edad entonces el apoyo será de $800")
elif Sexo=="mujer" and Hijos==1 and Edad>=18:
    print("Eres mujer, tienes un hijo y eres mayor de edad entonces el apoyo será de $300")
elif Sexo=="mujer" and Hijos>1 and Edad<=18:
    print("Eres mujer, tienes más de un hijo y eres menor de edad entonces el apoyo es de $1500")
elif Sexo=="mujer" and Hijos>1 and Edad>=18:
    print("Eres mujer, tienes más de un hijo y ya eres mayor de edad entonces el apoyo es de $500")
elif Sexo=="hombre" and Hijos>=1 and EstadoCivil=="soltero":
    print("Eres hombre y tienes hijos el apoyo es de $780")
else:
    print("No Válido")