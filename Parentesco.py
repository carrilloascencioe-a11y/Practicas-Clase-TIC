parentesco=input("¿Qué eres mío? ")
if parentesco=="hermano" or parentesco=="Hijo":
   print("Eres de mi Familia")
else:
   print("No eres de mi familia")
#REALIZA UN PROGRAMA QUE INDIQUE SI UNA PERSONA PUEDE O NO ENTRAR A UN CONCIERTO
Edad=int(input("Ingresa tu Edad "))
PermisoPadres=input("Ingresa Si Tienes o No Permiso de tus Padres ")
Acompañado=input("Ingresa si estas Acompañado ")
if Edad>=18 or PermisoPadres=="si":
   print("Puedes Entrar al Concierto")
elif Edad>=18 or Acompañado=="si":
   print("Puedes Entrar al Conciento")
else:
   print("No Puedes Entrar al Concierto")

