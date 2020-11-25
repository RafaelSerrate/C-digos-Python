sal = float(input('Coloque o salario do funcionario: R$'))
if sal > 1250.00:
    print('O salário com 10% de aumento vai ser {}'.format(sal+(sal * (10/100))))
else:
    print('O salário com 15% de aumento vai ser {}'.format(sal+(sal * (15/100))))
