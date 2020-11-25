from random import randint
from time import sleep
numeropc = randint(0, 5)
numeropessoa = int(input('O computador pensou em um numero entre 0 e 5. Tente adivinhar!: '))
while numeropessoa > 5 or numeropessoa < 0:
    numeropessoa = int(input('Coloque um numero inteiro entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if numeropessoa == numeropc:
    print('Você acertou, parabens!!')
else:
    print('Você errou :(')
    print('Eu pensei no numero {}'.format(numeropc))
