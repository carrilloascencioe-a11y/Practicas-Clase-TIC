#Programa que agrega películas a una lista
#Ponerle nombre a mi lista
Pelicula=[]
#Preguntar cuantas peliculas
CanPelis=int(input("Cuantas PelÍculas vas a Agregar"))
#Valor inicial para el while
i=0
#Mientras i sea menor a cantidad ejecutar
while i<=CanPelis:
    #Preguntar peliculas
    peli=input("Ingresa Películas: ")
    #Agregar peliculas a la lista
    Pelicula.append(peli)
    #Muestra la lista
    print(Pelicula)
    i=i+1
#Buscar una pelicula en la lista
#Preguntar la peli a buscar
PeliBuscar=input("Qué Película Buscas ")
if PeliBuscar in Pelicula:
    print("Si esta")
else:
    print("No esta pero dejame la agrego")
    Pelicula.append(PeliBuscar)
    print(Pelicula)
#lo extra
#solicitar una pelicula para borrar
#Borrar la película
#Muestra la lista
Peliculas=[]
ListaPelis=int(input("Cuantas vas a agregar"))
i=0
while i<=ListaPelis:
    pelis=input("Ingresa Películas: ")
    Peliculas.append(pelis)
    print(Peliculas)
    i=i+1
PeliBorrar=input("Cual quieres borrar")
print(Peliculas)
Peliculas.remove(PeliBorrar)
for Pelis in Peliculas:
    print(Peliculas)