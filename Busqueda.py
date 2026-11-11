Nombres=["Angel","Karla","Luis","Mateo","Maria","Luis","Karla"]
print(f'Los Nombres que se tienen son:{Nombres}')
NombreBuscar=input("¿Qué Nombre Deseas Buscar")
Encontrado=False
Contador=0
i=0
while i<len(Nombres):
    if Nombres[i]==NombreBuscar:
        Encontrado=True
        Contador=Contador+1
        print("Encontrado en la posicón:",i)
        i=i+1
        if Encontrado==True:
            print("Nombre Encontrado")
            print("Aparece",Contador,"Veces")
        else:
            print("Nombre no Encontrado")

