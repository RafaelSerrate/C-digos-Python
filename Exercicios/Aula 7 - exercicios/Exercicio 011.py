alt = float(input('Coloque a altura da parede em metros: '))
larg = float(input('Coloque a larguda da parede em metros: '))
area = alt * larg
print('Sua parede tem area de {}'.format(area))
print('Precisa-se {} litro(s) de tinta para pintar essa parede.'.format(area/2))