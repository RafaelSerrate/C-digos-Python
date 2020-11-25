dia = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
valor = (dia*60) + (km*0.15)
print('O total a pagar é de {:.2f}'.format(valor))
