print ("Conversor de Moedas: ")

cotacao = {'DOLAR': [5.15, '$'], 'EURO': [6.30, '€'], 'LIBRA': [7.10, '£']}

valor = float(input("Valor a ser Convertido: "))
moeda = input("Converter R$ em Dolar, Euro ou Libra: ").upper()

if moeda in cotacao.keys():
    n = valor / cotacao[moeda][0]
    print(f"O valor de {valor} R$ equivale a {round(n,2)} {cotacao[moeda][1]}")
else:
    print('Moda não encontrada')
