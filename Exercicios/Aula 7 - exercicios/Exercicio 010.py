din = float(input('Quanto dinheiro você tem? R$'))
dolar = din / 4.02
euro = din / 4.52
print('Com R${:.2f} você consegue comprar US${:.2f} e {:.2f } euros'.format(din, dolar, euro))