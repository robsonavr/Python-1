print ("Conversor de Moedas: ")

valor = float(input("Valor a ser Convertido: "))
moeda = input("Converter R$ em Dolar, Euro ou Libra: ").upper()

if (moeda == "DOLAR"):
    n = valor/5.15
    print(f"O valor de {valor} R$ equivale a {round(n,2)} $")
    #round(numero_flutunate, 2) escrever apenas os 2 primeiros numeros pos o ponto
elif (moeda == "EURO"):
    n = valor/6.30
    print(f"O valor de {valor} R$ equivale a {round(n,2)} €")
elif (moeda == "LIBRA"):
    n = valor/7.10
    print(f"O valor de {valor} R$ equivale a {round(n,2)} £")
else:
    print ("ERRO")
