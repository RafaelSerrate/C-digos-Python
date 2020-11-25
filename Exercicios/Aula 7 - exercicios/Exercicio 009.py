num = int(input('Coloque um numero: '))
cont = 0
result = 0

while cont < 11:
    result = num*cont
    print('{} vezes {}: {}'.format(num, cont, result))
    cont += 1

print('\n')

result2 = 0

for i in range(0, 11):
    result2 = i * num
    print('{} vezes {}: {}'.format(num, i, result2))

print('\n')

print('{} vezes 0: {}'.format(num, num*0))
print('{} vezes 1: {}'.format(num, num*1))
print('{} vezes 2: {}'.format(num, num*2))
print('{} vezes 3: {}'.format(num, num*3))
print('{} vezes 4: {}'.format(num, num*4))
print('{} vezes 5: {}'.format(num, num*5))
print('{} vezes 6: {}'.format(num, num*6))
print('{} vezes 7: {}'.format(num, num*7))
print('{} vezes 8: {}'.format(num, num*8))
print('{} vezes 9: {}'.format(num, num*9))
print('{} vezes 10: {}'.format(num, num*10))