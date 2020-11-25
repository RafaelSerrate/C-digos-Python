viagem = float(input('Coloque a distância da sua viagem em Km: '))
if viagem <= 200:
    preco1 = 0.5 * viagem
    print('O preço da viagem vai ser de R${}'.format(preco1))
else:
    preco2 = 0.45 * viagem
    print('O preço da viagem vai ser de R${}'.format(preco2))
