from random import choice
a1 = input('Coloque o nome do primeiro aluno: ')
a2 = input('Coloque o nome do segundo aluno: ')
a3 = input('Coloque o nome do terceiro aluno: ')
a4 = input('Coloque o nome do quarto aluno: ')
esc = choice([a1, a2, a3, a4])
print('O aluno escolhido é {}'.format(esc))