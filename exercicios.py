'''
 1. Classe Pessoa:  Crie uma classe Pessoa com os atributos nome e idade.
Crie um método que exiba uma mensagem: “Olá, meu nome é [nome] e tenho [idade] anos.”
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

'''
2. Classe Carro: Crie uma classe Carro que tenha modelo, ano e velocidade.
Adicione métodos acelerar() e frear().

'''
class Carro:
    def __init__(self, modelo, ano, velocidade=0):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10
        print(f"O carro acelerou. Velocidade atual: {self.velocidade} km/h")

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            self.velocidade = 0
        print(f"O carro freiou. Velocidade atual: {self.velocidade} km/h")

'''
3. Classe Conta: Crie uma classe Conta com saldo e métodos depositar() e sacar().
'''

class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente!")

'''
4. Classe Animal: Crie uma classe Animal com método falar().
'''

class Animal:
    def falar(self):
        print("O animal fez um som.")

'''
5. Classe Produto: Crie uma classe Produto com atributos nome e preço. Crie um método desconto(percentual).
'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        novo_preco = self.preco - (self.preco * percentual / 100)
        print(f"Preço com desconto: R${novo_preco:.2f}")

'''
6. Classe Livro: Crie uma classe Livro com título, autor e método exibir_detalhes().
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        print(f"Título: {self.titulo} | Autor: {self.autor}")

'''
7. Classe Aluno: Crie uma classe Aluno com nome, nota e método resultado() que diga se passou (nota ≥ 7).
'''

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def resultado(self):
        if self.nota >= 7:
            print(f"{self.nome} passou com nota {self.nota}.")
        else:
            print(f"{self.nome} não passou. Nota: {self.nota}.")

'''
8. Classe Calculadora: Crie uma classe Calculadora com métodos somar, subtrair, multiplicar, dividir.
'''

class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero"

'''
9. Classes Funcionario e Gerente: Crie uma classe Funcionario e uma classe Gerente que herda de Funcionario e adiciona o atributo setor.
'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

'''
10. Classe Retangulo: Crie uma classe Retangulo com base e altura e método area().
'''

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
