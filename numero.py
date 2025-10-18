"""
Instruções
História:

A empresa AWXS é um novo cliente da JWC, uma empresa especializada em desenvolvimento de soluções personalizadas. Após o sucesso da primeira fase do jogo "Número Secreto" durante a Aula 01, a JWC está em fase probatória para demonstrar sua competência no desenvolvimento de projetos interativos.

Agora é o momento de avançar para a Fase 2 do jogo, implementando novos desafios e funcionalidades que tornarão o jogo ainda mais interessante. Para isso, o cliente solicitou a adição de um sistema de níveis de dificuldade e um sistema de pontuação que premia a precisão dos jogadores.

Objetivos da Fase 2:
Implementar o sistema de níveis de dificuldade:

Fácil: O jogador tem 30 tentativas para adivinhar o número secreto.
Médio: O jogador tem 15 tentativas para adivinhar o número secreto.
Difícil: O jogador tem 5 tentativas para adivinhar o número secreto.
Implementar o sistema de pontuação:

O jogador começa com uma pontuação inicial de 100 pontos.
A cada tentativa errada, o jogador perde pontos.
O cálculo da pontuação perdida pode ser adaptado ao nível de dificuldade. Por exemplo:
Fácil: Perde 10 pontos por erro.
Médio: Perde 20 pontos por erro.
Difícil: Perde 50 pontos por erro.
Garantir que o jogador seja informado sobre sua pontuação e tentativas restantes após cada tentativa.
"""

print("Bem-vindo ao jogo Número Secreto - Fase 2!")

print("Escolha o nível de dificuldade:")
print("1 - Fácil (30 tentativas, -10 pontos por erro)")
print("2 - Médio (15 tentativas, -20 pontos por erro)")
print("3 - Difícil (5 tentativas, -50 pontos por erro)")

while True:
    nivel = input("Digite 1, 2 ou 3: ")
    if nivel == "1":
        tentativas = 30
        perda_por_erro = 10
        break
    elif nivel == "2":
        tentativas = 15
        perda_por_erro = 20
        break
    elif nivel == "3":
        tentativas = 5
        perda_por_erro = 50
        break
    else:
        print("Escolha inválida. Tente novamente.")

numero_secreto = 28
pontuacao = 100

while tentativas > 0:
    print("\nTentativas restantes:", tentativas)
    print("Pontuação atual:", pontuacao)
    
    palpite = input("Digite seu palpite (1-100): ")
    
    if not palpite.isdigit():
        print("Digite um número válido!")
        continue
    
    palpite = int(palpite)
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        print("Sua pontuação final é:", pontuacao)
        break
    else:
        tentativas = tentativas - 1 
        pontuacao = pontuacao - perda_por_erro  
        if pontuacao < 0: 
            pontuacao = 0

        if palpite < numero_secreto:
            print("O número secreto é maior!")
        else:
            print("O número secreto é menor!")

        if tentativas == 0:
            print("Suas tentativas acabaram! O número secreto era:", numero_secreto)
            print("Sua pontuação final é:", pontuacao)
