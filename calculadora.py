def calculadora(n1,n2):
    soma = n1+n2
    print ("Soma: ",soma)
    subtracao = n1-n2
    print ("Subtracao:  ",subtracao)
    multiplicacao = n1*n2
    print ("Multiplicacao:  ",multiplicacao)
    if (n2!=0):
        divisao = n1/n2
        print ("Divisao:  ",divisao)
    else :
        print ("Divisao invalida")

n1 = float (input ("Digite um valor : "))
n2 = float (input ("Digite outro  valor : "))
print ("\n")
calculadora(n1,n2)
