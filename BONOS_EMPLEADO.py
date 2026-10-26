Nombre=input("Ingresa el Nombre del Empleado")
PagoHora=float(input("Ingresa el Pago por Hora del Empleado"))
HorasTrabajo=int(input("Ingresa las Horas de Trabajo al Mes"))
Sueldo=(PagoHora*HorasTrabajo)
print("Tu Sueldo es", Sueldo) 
Bono1=int=500
Bono2=int=1700
Bono3=int=3500
Bono4=int=8500
Bono5=int=10000
sueldoBono1=(Bono1+Sueldo)
sueldoBono2=(Bono2+Sueldo)
sueldoBono3=(Bono3+Sueldo)
sueldoBono4=(Bono4+Sueldo)
sueldoBono5=(Bono5+Sueldo)
if Sueldo>=100 and Sueldo<=300:
     print("Tu Sueldo con Bono es", sueldoBono1)
elif Sueldo>300 and Sueldo>=1500:
     print("Tu Sueldo con Bono es", sueldoBono2)
elif Sueldo>1500 and Sueldo<3000:
     print("Tu Sueldo con Bono es", sueldoBono3)
elif Sueldo>3000 and Sueldo<8000:
     print("Tu Sueldo con Bono es", sueldoBono4)
elif Sueldo>8000:
     print("Tu Sueldo con Bono es", sueldoBono5)