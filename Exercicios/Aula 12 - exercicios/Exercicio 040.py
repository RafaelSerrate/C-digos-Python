n1 = float(input('Coloque a primeira nota: '))
n2 = float(input('Coloque a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Reprovado!')
elif media >= 5 and 6.9 >= media:
    print('Recuperação!')
else:
    print('Aprovado!')
