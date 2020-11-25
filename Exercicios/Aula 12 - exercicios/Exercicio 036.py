valorcasa = float(input('Coloque o preço da casa: R$'))
salario = float(input('Coloque o salário: R$'))
anos = int(input('Coloque quantos anos você quer financiar a casa: '))
prestacao = valorcasa / (anos * 12)
print("Para pagar uma casa de R${:.2f} em {} anos e a ".format(valorcasa, anos), end='')
print("prestação sera de R${:.2f}".format(prestacao))
minimo = salario * (30/100)
if prestacao > salario * (30/100):
    print("Emprestimo NEGADO")
    print("Exedeu, a prestação é de {} e o minimo é de {}".format(prestacao, minimo))
else:
    print("Emprestimo ACEITO")
    print("A prestação é de {:.2f} e o minimo é de {:.2f}".format(prestacao, minimo))
