import math
adj = float(input('Coloque o valor do cateto adjacente: '))
ops = float(input('Coloque o valor do cateto oposto: '))
hip = pow(pow(adj, 2)+pow(ops, 2), (1/2))
print('A hipotenusa é {:.2f}'.format(hip))
print('\n\n')
ca = float(input('Coloque o valor do cateto adjacente: '))
co = float(input('Coloque o valor do cateto oposto: '))
hi = math.hypot(ca, co)
print('A hipotenusa é {:.2f}'.format(hi))