numero_secreto = 8

tentativa = int(input("Tente adivinhar o número secreto: "))

if tentativa == numero_secreto:
    print("Parabéns, você acertou o número secreto!")
elif tentativa < numero_secreto:
    print(f"Errou! O número secreto é maior que {tentativa}.")
else:
    print(f"Errou! O número secreto é menor que {tentativa}.")