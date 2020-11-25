r1 = float(input('Coloque o comprimento da primeira reta: '))
r2 = float(input('Coloque o comprimento da segunda reta: '))
r3 = float(input('Coloque o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Da para fazer um triângulo com os comprimentos {}, {} e {}'.format(r1, r2, r3))
else:
    print('Não da para fazer um triângulo com os comprimentos {}, {} e {}'.format(r1, r2, r3))
