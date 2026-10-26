Nombre=input("Ingresa el Nombre del Empleado")
PagoHora=float(input("Ingresa el Pago por Hora del Empleado"))
HorasTrabajo=int(input("Ingresa las Horas de Trabajo al Mes"))
Sueldo=(PagoHora*HorasTrabajo)
print("Tu Sueldo es", Sueldo) 
if Sueldo>=100 and Sueldo<=300:
    Bono1=500
    sueldoBono1=(Bono1+Sueldo)
    print("Tu Sueldo con Bono es", sueldoBono1)
elif Sueldo>300 and Sueldo>=1500:
     Bono2=1700
     sueldoBono2=(Bono2+Sueldo)
     print("Tu Sueldo con Bono es", sueldoBono2)
elif Sueldo>1500 and Sueldo<3000:
     Bono3=3500
     sueldoBono3=(Bono3+Sueldo)
     print("Tu Sueldo con Bono es", sueldoBono3)
elif Sueldo>3000 and Sueldo<8000:
     Bono4=8500
     sueldoBono4=(Bono4+Sueldo)
     print("Tu Sueldo con Bono es", sueldoBono4)
elif Sueldo>8000:
     Bono5=10000
     sueldoBono5=(Bono5+Sueldo)
     print("Tu Sueldo con Bono es", sueldoBono5)