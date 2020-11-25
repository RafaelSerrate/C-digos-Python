from random import choice
print('JOGO JOKENPÔ\n\n')
print('PEDRA')
print('PAPEL')
print('TESOURA')
jogador = input('QUAL VOCÊ QUER JOGAR? ').strip().upper()
while not jogador == 'PEDRA' and not jogador == 'PAPEL' and not jogador == 'TESOURA':
    input('Qual você quer jogar? ').strip().upper()
computador = choice(['PEDRA', 'PAPEL', 'TESOURA'])
print('\n')
print('VOCÊ ESCOLHEU {}'.format(jogador))
print('O COMPUTADOR ESCOLHEU {}'.format(computador))
print('\n')
if computador == jogador:
    print('A PARTIDA EMPATOU')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('O JOGADOR GANHOU')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('O COMPUTADOR GANHOU')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('O COMPUTADOR GANHOU')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('O JOGADOR GANHOU')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('O JOGADOR GANHOU')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('O COMPUTADOR GANHOU')
else:
    print('ALGO DEU ERRADO')
