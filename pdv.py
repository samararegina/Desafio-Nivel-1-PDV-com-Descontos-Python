compras = []
desconto_20 = 0.2
desconto_10 = 0.1
valor_total_bruto = 0.0
valor_total_com_desconto = 0.0
valores_com_desconto = []
qnt_descontos = 0

idade_cliente = int(input("Digite a sua idade: "))

while idade_cliente < 0 :
     print("\nIdade Inválida !!")
     idade_cliente = int(input("Digite uma Idade Válida: "))

print()

loop = True
qnt = 0

while loop:
    print("="*10+" PDV com Descontos "+"="*10)
    print("Escolha: ")
    print("1 - Fazer Compra")
    print("0 - Encerrar Compra")

    opcao = input("Opção: ")

    while opcao != "1" and opcao != "0":
        print("\nValor inválido !!")
        opcao = input("Digite uma Opção Válida: ")

    print()

    if opcao == "1":
        qnt+=1
        print(f"{qnt}ª Compra:")
        valor_compra = float(input("Digite o valor (00.00): "))

        compras.append(valor_compra)

        print()

    elif opcao == "0":
            loop=False


valor_total_bruto = sum(compras)

if idade_cliente >=65:
    for compra in compras:
        valor_desconto_idade = compra * desconto_20
        valor_final_com_desconto = compra - valor_desconto_idade

        qnt_descontos+=1

        if valor_final_com_desconto > 100:
            valor_desconto_idade_extra = valor_final_com_desconto * desconto_10
            valor_final_com_desconto-=valor_desconto_idade_extra
            
            qnt_descontos+=1

        valores_com_desconto.append(valor_final_com_desconto)
    
    valor_total_com_desconto = sum(valores_com_desconto)

else:
    for compra in compras:
        valor_final_com_desconto = compra

        if compra > 100:
            valor_desconto_por_valor = compra * desconto_10
            valor_final_com_desconto = compra - valor_desconto_por_valor
            
            qnt_descontos += 1

        valores_com_desconto.append(valor_final_com_desconto)

    valor_total_com_desconto = sum(valores_com_desconto)

total_descontos = valor_total_bruto - valor_total_com_desconto

print("-"*15 + " Resumo do Dia " + "-"*15)
print(f"Idade do cliente = {idade_cliente}")
print(f"Quantidade de compras registradas = {qnt}")
print(f"Total bruto = R${valor_total_bruto:.2f} ")
print(f"Total de descontos concedidos = {qnt_descontos}")
print(f"Total de descontos concedidos em R$ = R${total_descontos:.2f}")
print(f"Total final com descontos = R${valor_total_com_desconto:.2f}")
     