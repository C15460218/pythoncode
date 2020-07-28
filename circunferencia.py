"""
Nombre: Circunferencia.py
Objetivo: Permite calcular el área de una circunferencia
Autor: Adrian Robles
FEcha: 20 de julio de 2020
"""

#Importamis libreria match
import math

#- - - - - - - - - - - - - - - - - - - -
#Función para calcular área
#- - - - - - - - - - - - - - - - - - - -
def calcularAre(valorRadio):
	return math.pi*math.pow(valorRadio,2)


# Módulo principal
def main():
	ciclo='S'
	while(ciclo=='S' or ciclo=='s'):
		print("- - - Programa para calcular Área de Circunferencia - - -")
		vradio = int(input("Introduce valor de radio: "))
		print("\n")
		print("EL área de la circunferencia con radio igual a: {}, es: {}".format(vradio,calcularAre(vradio)))
		ciclo=input("¿Desea otra operación? (S/N): ")


if __name__ == "__main__":
	main()
