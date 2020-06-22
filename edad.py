#Autor: Edwin Hernandez
#Calcula tu edad de año actual

anio_actual = 2020 
nombre = input("Cuál es tu nombre?: ") 
mes_actual = 6
anio_nacimiento = int(input("En qué año naciste? : "))
mes_nacimiento = int(input("En qué mes naciste [ 1-12]? : "))
edad = anio_actual - anio_nacimiento 
if mes_nacimiento > mes_actual:
	edad -=1

print("\n Hola",nombre,"tu edad en este año es:",edad);


