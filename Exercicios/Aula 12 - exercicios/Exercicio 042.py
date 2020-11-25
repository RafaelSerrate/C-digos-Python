reta1 = float(input('Coloque o comprimento da primeira reta: '))
reta2 = float(input('Coloque o comprimento da segunda reta: '))
reta3 = float(input('Coloque o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Da para formar um triangulo com esses comrpimentos.')
    if reta1 == reta2 == reta3:
        print('Esse triângulo é EQUILÁTERO!')
    elif reta1 == reta2 != reta3 or reta1 != reta2 == reta3 or reta1 != reta3 == reta2 or reta1 == reta3 != reta2:
        print('Esse triângulo é ISÓSCELES!')
    elif reta1 != reta2 != reta3:
        print('Esse triângulo é ESCALENO!')
    else:
        print('QUEBRO')
else:
    print('Não da para formar um triangulo com esses comrpimentos.')
