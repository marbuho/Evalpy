import sys
from evalpy.darcambio import darcambio
from evalpy.bala_corch import bala_corch

def main():

	argv = sys.argv[1:]
	if (len(argv))==0 or ((len(argv))=="-h"):
		print("use -h para obtener ayuda")
	else:

		if argv[0] == '-c':
			result = darcambio(int(argv[1]), int(argv[2]))
			print("su cambio es: ",result)

		elif argv[0] == '-b':
			result = bala_corch(argv[1])
			print(result)
		else: 
			print("El programa calcula el cambio a dar o analiza si una exp de corchetes esta balanceada:\npara ellos se admite las siguientes entredas\n calcular cambio: -c <n1>  <n2>   n1: cantidad con la que se abona\ n2:cantidad a pagar\n Analizar corchetes -b <corch>\
			corch: expresion de corchetes(ej: [][][][)")				
if __name__ == "__main__":
		main()