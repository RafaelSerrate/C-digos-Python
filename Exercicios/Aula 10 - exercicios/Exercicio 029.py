vlcarro = float(input('Coloque a velocidade do carro em km/h: '))
if vlcarro > 80:
    print('Esse carro ultrapassou o limite de velocidade, ele sera multado.')
    multa = (vlcarro - 80) * 7
    print('A multa sera de R${}'.format(multa))
else:
    print('Esse carro esta na velocidade permitida.')
