estoque = int(input("Digite a quantidade inicial de produtos em estoque: "))

while True:
    operacao = input("\nDigite 'venda' para registrar uma venda, 'reposicao' para adicionar produtos ou 'sair' para encerrar: ").lower()

    if operacao == "venda":
        quantidade = int(input("Quantos produtos foram vendidos? "))
        if quantidade <= estoque:
            estoque -= quantidade
            print(f"Venda registrada. Estoque atual: {estoque}")
        else:
            print("Estoque insuficiente para essa venda!")
    elif operacao == "reposicao":
        quantidade = int(input("Quantos produtos foram adicionados ao estoque? "))
        estoque += quantidade
        print(f"Reposição registrada. Estoque atual: {estoque}")
    elif operacao == "sair":
        break
    else:
        print("Opção inválida. Tente novamente.")

print(f"\n✅ Saldo final de produtos em estoque: {estoque}")