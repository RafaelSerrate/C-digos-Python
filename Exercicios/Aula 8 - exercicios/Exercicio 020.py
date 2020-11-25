from random import shuffle, sample
a1 = input('Coloque o nome do primeiro aluno: ')
a2 = input('Coloque o nome do segundo aluno: ')
a3 = input('Coloque o nome do terceiro aluno: ')
a4 = input('Coloque o nome do quarto aluno: ')
deck = [a1, a2, a3, a4]
shuffle(deck)
print('A ordem de a presentação vai ser {}'.format(deck))