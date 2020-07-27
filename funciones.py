"""
Nombre funciones.py
Objetivo: muestra las operaciones de las funciones de python
Autor: Adrian Robles
Fecha: 27 julio de 2020
"""

def mensaje():
	print("hola desde mensaje")

def regresaMensaje():
	return "saludo desde regresaMensaje"

def printMensaje(msg):
	print(msg)

def suma(n1,n2):
	return n1+n2

def resta():
	return n1-n2

def multiplicacion(n1,n2):
	return n1*n2

def division(n1,n2):
	return n1/n2

def main():
	ciclo='S'
	while ciclo == 'S' or ciclo == 's':
		#invocamos funcion mensaje
		mensaje()
		#invocamos funcion regresaMensaje()
		print(regresaMensaje())
		#invocamos funcion printMensaje()
		printMensaje("saludodes de printMensaje")
		#Leemos los datos por teclado
		a = int(input("Ingresa el primer entero: "))
		b = int(input("Ingresa el segundo entero: "))
		#Invocamos la función suma
		print("La suma es: ", suma(a,b))
		#Invocamos la funcion resta
		print("La resta es: ", resta(a,b))
		#Invocamos la funcion multiplicación
		print("La multiplicación es: ", multiplicacion(a,b))
		#invocamos la funcion división
		print("La división es: ",division(a,b))
		#Preguntamos por otra operación
		ciclo = input("¿Desea otra operación? (S/N): ")
	else:
		print("*** fin del programa")

if __name__ == "__main__":
	main()
