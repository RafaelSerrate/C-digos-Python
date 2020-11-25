num = int(input('Coloque um numero inteiro: '))
while not num == int(num):
    input('Coloque um numero inteiro: ')
print('1) Binário')
print('2) Octal')
print('3) Hexadecimal')
conversor = int(input('Escolha um dos conversores acima: '))
while not conversor == 1 or not conversor == 2 or not conversor == 3:
    conversor = int(input('Escolha um dos conversores acima: '))
if conversor == 1:
    print('seu numero sera convertido em binario')

elif conversor == 2:
    print('Seu numero sera convertido em octal')
else:
    print('Seu numero sera convertido em hexadecimal')
print('A conversao do seu número vai ser: {}'.format())
