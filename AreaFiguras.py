#Programa para calcular áreas
#Área cuadrado; lado x lado
lado=float(input("ingresa lado"))
AreaCuadrado=lado*lado
print("El Área es", AreaCuadrado)
print(F'El área es {AreaCuadrado}')
#ÁREA DE TRIANGULO
Base=float(input("Ingresa Base"))
Altura=float(input("Ingresa Altura"))
AreaTriangulo=(Base*Altura)/2
print("El Área es", AreaTriangulo)
#ÁREA DEL TRAPECIO
BaseM=float(input("Ingresa la Base Mayor"))
base=float(input("Ingresa la Base Menor"))
Altura=float(input("Ingresa la Altura"))
AreaTrapecio=(BaseM+base)*Altura/2
print("El Área es", AreaTrapecio)
#ÁREA DEL CIRCULO
PI=(3.1416)
Radio=float(input("Ingresa el Radio"))
AreaCirculo=PI*(Radio*Radio)
print("El Área es", AreaCirculo)
#ÁREA DEL PENTAGONO
Perimetro=float(input("Ingresa el Perimetro"))
Apotema=float(input("Ingresa la Apotema"))
AreaPentagono=(Perimetro*Apotema)/2
print("El Área es", AreaPentagono)