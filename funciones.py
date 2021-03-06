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

def resta(n1,n2):
	return n1-n2

def multiplicacion(n1,n2):
	return n1*n2

def division(n1,n2):
	if(n2!=0):
		return n1/n2
	else:
		print("Error no se puede dividir entre 0")

def compara(n1,n2):
	if n1>n2:
		print("EL mayor es n1: ", n1," ", n2)
	elif n2>n1:
		print("EL mayor es: {},{}".format(n2,n1))
	else:
		print("Los numeros son iguales:{}, {}".format(n1,n2))

def cuenta(n1,n2):
	if (n2>n1):
		for i in range(n1,n2+1):
			print("Valor de i: {}".format(i))
	elif (n1>n2):
		for i in range(n1,n2-1,-1):
			print("valor de i: {}".format(i))
	else:
		print("LOs numeros son iguales, no puedo contar: {}, {}".format(n1,n2))

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
		compara(a,b)
		cuenta(a,b)
		#Preguntamos por otra operación
		ciclo = input("¿Desea otra operación? (S/N): ")
	else:
		print("*** fin del programa")

if __name__ == "__main__":
	main()
