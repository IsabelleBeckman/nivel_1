historico_compras = []

while True:
    valor = float(input("Digite o valor da compra (ou 0 para encerrar): "))
    if valor == 0:
        break
        
    idade = int(input("Digite a idade do cliente: "))
    quantidade = int(input("Digite a quantidade de itens: "))
    cupom = input("Digite o cupom de fidelidade (ou deixe em branco): ").strip().upper()
    
    if valor < 0 or idade < 0 or quantidade < 0:
        print("Aviso: Valores não podem ser negativos. Tente novamente.")
        continue
        
    valor_descontado = valor
    
    # Regras principais
    if idade >= 65:
        valor_descontado *= 0.80
        
    if valor_descontado > 100:
        valor_descontado *= 0.90
        
    # Bônus 1: Desconto por quantidade
    if quantidade > 3:
        valor_descontado *= 0.95
        
    # Bônus 2: Cupom de fidelidade
    if cupom == "FIDELIDADE10":
        valor_descontado *= 0.90
        
    print(f"Valor final: R$ {valor_descontado:.2f}\n")
    
    historico_compras.append({
        "valor_bruto": valor,
        "desconto_total": valor - valor_descontado,
        "valor_liquido": valor_descontado
    })

# Resumo Final e Bônus 3 (Gravar arquivo)
qtd_compras = len(historico_compras)

if qtd_compras > 0:
    total_bruto = sum(compra["valor_bruto"] for compra in historico_compras)
    total_descontos = sum(compra["desconto_total"] for compra in historico_compras)
    total_liquido = sum(compra["valor_liquido"] for compra in historico_compras)
    
    # Exibe no terminal
    resumo_texto = (
        "--- Resumo do Dia ---\n"
        f"Quantidade de compras registradas: {qtd_compras}\n"
        f"Total bruto: R$ {total_bruto:.2f}\n"
        f"Total de descontos concedidos: R$ {total_descontos:.2f}\n"
        f"Total final: R$ {total_liquido:.2f}\n"
    )
    print(resumo_texto)
    
    # Grava no txt
    with open("resumo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(resumo_texto)
        arquivo.write("\n--- Detalhamento das Compras ---\n")
        for i, compra in enumerate(historico_compras, 1):
            arquivo.write(
                f"Compra {i}: Bruto R$ {compra['valor_bruto']:.2f} | "
                f"Desconto R$ {compra['desconto_total']:.2f} | "
                f"Líquido R$ {compra['valor_liquido']:.2f}\n"
            )
    print("Histórico salvo com sucesso no arquivo 'resumo.txt'.")
else:
    print("Nenhuma compra registrada.")