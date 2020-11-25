soma = 0
for n in range(0, 6):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma = num + soma
print('A soma dos números pares foram: {}'.format(soma))
