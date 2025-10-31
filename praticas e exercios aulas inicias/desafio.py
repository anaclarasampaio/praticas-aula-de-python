numero = int(input('Digite um número: '))

if numero %2 == 0:
    print("O número " + str(numero) + " é par")
else: 
    print("O número: " + str(numero) + " é ímpar")




idade = int(input('Digite a sua idade: '))

if idade<=12:
    print("Você é uma criança")
elif idade<=18:
    print("Você é um adolescente")
else:
    print("Você é um adulto")

nota1 = float(input('Digite sua nota 1: '))
nota2 = float(input('Digite sua nota 2: '))
media = (nota1 + nota2)/2

if media >=7:
    print("Você está aprovado")
elif media >=5: 
    print("Você está em recuperação")
else:
    print("Você está reprovado")

