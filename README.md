**O que o código faz**
O script opera como um Ponto de Venda (PDV) automatizado que aplica descontos progressivos baseados na idade do cliente, no montante da compra, na quantidade de itens e em cupons de fidelidade. Ao encerrar as atividades, gera um resumo financeiro diário no terminal e guarda o histórico num ficheiro de texto.

**Como ele faz**
1. Recebe o valor da compra, a idade do cliente, a quantidade de itens e um cupons de fidelidade.
2. Valida se os valores numéricos são negativos; se forem, bloqueia a operação e reinicia o ciclo com um aviso.
3. Verifica se a idade é maior ou igual a 65 anos para aplicar um desconto inicial de 20%.
4. Verifica se o valor resultante ultrapassa 100 reais, concedendo um desconto adicional de 10%.
5. Aplica 5% de desconto extra se a quantidade de itens for superior a 3.
6. Aplica 10% de desconto extra se o cupons inserido for "FIDELIDADE10".
7. Exibe o valor final formatado e guarda os dados da transação numa lista.
8. Ao digitar 0 no valor da compra, encerra o ciclo, exibe o extrato e utiliza a função open() para gravar o detalhamento no ficheiro resumo.txt.

**Como rodar**
No terminal, navegue até à pasta nivel_1 e execute o comando: python pdv.py

**Tabela de exemplos**
| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---|---|---|---|---|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 100.00 | 65 | 20% | 0% | R$ 80.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10| 200.00 | 64 | 0% | 10% | R$ 180.00 |