princ = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peoso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    res = str(input('Deseja continuar? '))
    if res in 'Nn':
        break

print(f'Os dados foram {princ}')
print('-=' *20)
print(f'Foram cadastradas {len(princ)} pessoas')
print('-=' *20)
print(f'O maior peso foi {maior} e o menor foi {menor}')
print('-=' *20)
