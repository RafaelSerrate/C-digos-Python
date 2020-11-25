peso = float(input('Coloque o seu peso kg: '))
altura = float(input('Coloque sua altura em metros: '))
imc = peso / (altura ** 2)
print('O seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')


if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
