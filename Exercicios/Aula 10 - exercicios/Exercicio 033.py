n1 = int(input('Coloque o primeiro numero: '))
n2 = int(input('Coloque o segundo numero: '))
n3 = int(input('Coloque o terceiro numero: '))
# verificando o menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificando o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero é {} e o menor é {}'.format(maior, menor))
