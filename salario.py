print ("+++++++++++++Calculo do Salario Liquido+++++++++++++")
print ("|Dados|")
nome = input("Nome:").title()
recebe_por_horas = float(input("Valor por horas Trabalhadas:"))
horas = int (input("Horas Trabalhadas no Mes:"))

salario_bruto = recebe_por_horas*horas
imposto_de_renda = salario_bruto*11/100
inss = salario_bruto*8/100
sindicato = salario_bruto*5/100
salario_liquido = salario_bruto -(imposto_de_renda+inss+sindicato)

print (f"{nome}\nDescontos:")
print (f"Salario Bruto: {salario_bruto} R$\nImposto de Renda: {imposto_de_renda} R$")
print (f"INSS: {inss} R$\nSindicato: {sindicato} R$")
print (f"Com todos essas Cobrancas seu Salario Liquido: {salario_liquido} R$")

