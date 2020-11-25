from datetime import datetime
nascimento = int(input('Coloque o ano que você nasceu: '))
idade = datetime.today().year - nascimento
if idade < 18:
    print('Você não precisa se alistar, ainda faltam {} ano(s)'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar :)')
else:
    print('Já passou da hora de se alistar, passou {} ano(s)'.format(idade - 18))
