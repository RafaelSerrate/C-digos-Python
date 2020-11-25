vlproduto = float(input('Valor produto: '))
print('Formas de pagamento')
print('[1] A vista dinheiro/cheque')
print('[2] A vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartao')
forma = int(input('Qual a forma de pagar? '))
if forma == 1:
    desconto = vlproduto - (vlproduto * (10/100))
    print('Sua compra de {} vai custar {} no final'.format(vlproduto, desconto))
elif forma == 2:
    desconto = vlproduto - (vlproduto * (5/100))
    print('Sua compra de {} vai custar {} no final'.format(vlproduto, desconto))
elif forma == 3:
    print('O preço continuara {}'.format(vlproduto))
else:
    parcela = int(input('Quantas parecelas? '))
    acrescimo = vlproduto + (vlproduto * (20/100))
    vlparcela = acrescimo / parcela
    print('Sua compra será parcelada em {} vezes de {} com juros'.format(parcela, vlparcela))
    print('Sua compra de {} vai passar a custar {}'.format(vlproduto, acrescimo))


