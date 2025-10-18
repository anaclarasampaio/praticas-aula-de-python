"""
Instruções
Objetivo: Desenvolver um jogo simples em Python chamado "Número Secreto", utilizando apenas variáveis e estruturas de decisão (if, elif, else).

Instruções
Descrição do Jogo:

O programa deve escolher um número secreto fixo (você pode definir o número no código, por exemplo, numero_secreto = 7).
O jogador deverá adivinhar qual é o número secreto, digitando sua tentativa no console.
Regras:

Se o jogador acertar o número, o programa deve exibir uma mensagem de parabéns: "Parabéns, você acertou o número secreto!".
Se o jogador errar, o programa deve informar se o número digitado foi maior ou menor que o número secreto.
Exemplo:
Entrada do jogador: 5
Saída do programa: "Errou! O número secreto é maior que 5."
O jogador terá apenas uma tentativa nesta fase do jogo.
Requisitos Técnicos:

Use apenas variáveis para armazenar valores e estruturas de decisão (if, elif, else).
Não utilize laços de repetição nesta etapa.
Dicas:

Para capturar a entrada do jogador, utilize a função input().
Não se esqueça de converter a entrada do jogador para o tipo correto (número).
Exemplo de Execução:

Tente adivinhar o número secreto: 5
Errou! O número secreto é maior que 5.
"""

numero_secreto = 7

tentativa = int(input("Tente adivinhar o número secreto: "))

if tentativa == numero_secreto:
    print("Parabéns, você acertou o número secreto!")
elif tentativa < numero_secreto:
    print(f"Errou! O número secreto é maior que {tentativa}.")
else:
    print(f"Errou! O número secreto é menor que {tentativa}.")
