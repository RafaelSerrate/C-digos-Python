n = int(input('Coloque um número: '))
cont = 0
resultado = 0
while cont < 11:
    resultado = cont * n
    print("{} x {} = {}".format(n, cont, resultado))
    cont += 1

print("\n\n")

cont = 0
resultado = 0

for c in range(0, 11):
    resultado = c * n
    print("{} x {} = {}".format(n, c, resultado))
