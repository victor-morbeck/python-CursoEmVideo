#Exercício Python 085:
#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#Mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]
#Esse formato elimina a necessidade de duas listas
valor = 0

for c in range(7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

#O método 'sorted' coloca altomaticamente os valores da lista em ordem crescente
print(f'Os valores pares foram: {sorted(valores[0])}')
print(f'Os valores ímpares foram: {sorted(valores[1])}')