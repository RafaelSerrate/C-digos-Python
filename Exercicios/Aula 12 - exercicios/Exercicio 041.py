idade = int(input('Coloque a idade do(a) atleta: '))
if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade == 20:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
