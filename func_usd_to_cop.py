# -*- coding: utf-8 -*-

def foreign_exchange_calculator(ammount):
	usd_to_col_rate =  3.0127


	return usd_to_col_rate * ammount

def run():
	print('C A L C U L A D O R A   D E  D I V I S A S')
	print('Convierte pesos colombianos a dolares.')
	print('')

	ammount = float(input('Ingresa la cantidad de pesos colombianos que quieres convertir: '))

	result = foreign_exchange_calculator(ammount)

	print('${} pesos colombianos son ${} dolares'.format(ammount, result))
	print('')

if __name__ == '__main__':
	run()
	print("Final / no se ejecuta")