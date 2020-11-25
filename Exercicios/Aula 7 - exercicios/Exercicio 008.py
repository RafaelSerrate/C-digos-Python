m = int(input('Coloque a distancia em metros: '))
cen = m * 100
mili = m * 1000
print('Em {} metros temos {} centimetros e {} milimetros'.format(m, cen, mili))
print('{}km | {}hm | {}dam | {}m | {}dm | {}cm | {}mm '.format(m/1000, m/100, m/10, m, m*10, m*100, m*1000))