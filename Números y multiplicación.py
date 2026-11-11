Numeros=[]
Resultados=[]
i=0
while i<5:
    Num=int(input("Ingresa un Número: "))
    Numeros.append(Num)
    i=i+1
Multiplicador=int(input("¿Por cúanto deseas Multiplicar?: "))
for Num in Numeros:
    Resultado=Num*Multiplicador
    Resultados.append(Resultado)
print("Números originales:", Numeros)
print("Resultados:", Resultado)
#Extra:
print(f'Lon Números de la lista son:{Numeros}')
NumBuscar=input("¿Qué Número Deseas Buscar?:")
Encontrado=False
Contador=0
i=0
while i<len(Numeros):
    if Numeros[i]==NumBuscar:
        Encontrado=True
        contador=contador+1
        i=i+1
        if Encontrado==True:
           print("Número Encontrado")
        else:
           print("Número No Encontado")