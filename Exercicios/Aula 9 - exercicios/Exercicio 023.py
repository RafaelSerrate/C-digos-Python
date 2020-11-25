num = int(input('Coloque um numero inteiro entre 0 a 9999: '))
while num < 0 or num > 9999:
    num = int(input('Coloque um numero inteiro entre 1 a 9999: '))
if num < 10:
    print('Unidade: {}'.format(num))
elif num < 100:
    num = str(num)
    num.split()
    print('Unidade: {}'.format(num[1]))
    print('Dezena: {}'.format(num[0]))
elif num < 1000:
    num = str(num)
    num.split()
    print('Unidade: {}'.format(num[2]))
    print('Dezena: {}'.format(num[1]))
    print('Centena: {}'.format(num[0]))
elif num < 10000:
    num = str(num)
    num.split()
    print('Unidade: {}'.format(num[3]))
    print('Dezena: {}'.format(num[2]))
    print('Centena: {}'.format(num[1]))
    print('Milhar: {}'.format(num[0]))
else:
    print('Algo esta de errado')

print('\n\n\n\n')

n = int(input('Coloque um numero de 0 ate 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o numero {}'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
