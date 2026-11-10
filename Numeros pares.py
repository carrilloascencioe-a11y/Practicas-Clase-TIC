Numeros=[]
i=0
while i<10:
    Num=int(input("Ingresa un Número: "))
    Numeros.append(Num)
    i=i+1
print("Números pares:")
for Num in Numeros:
    if Num%2==0:
       print(Num)
