cidade = input('Coloque o nome da sua cidade: ').strip()
print(cidade.upper()[:5] == 'SANTO')

cid = str(input('Coloque o nome da sua cidade: ')).strip().upper().split()
print('SANTO' in cid[0])
