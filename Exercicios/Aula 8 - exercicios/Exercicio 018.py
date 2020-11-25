from math import sin, cos, tan, radians
ang = float(input('Coloque um angulo qualquer: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('o angulo {} graus tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(ang, seno, cosseno, tangente))
