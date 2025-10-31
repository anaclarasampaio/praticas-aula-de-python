class Carro: 
    def __init__(self,nome,cor):
        self.nome = nome  #atributo
        self.cor = cor #atributo 
        self.velocidade = 0 #atrinuto inical 

    def acelerate(self):
        self.velocidade += 10
        print(f"{self.nome} está a {self.velocidade} km/h")

    def frear(self):
        self.velocidade -= 10
        print(f"{self.nome} reduziu para {self.velocidade} km/h")

carro1 = Carro("Fusca", "Azul")
carro2 = Carro("Gol", "Vermelho")
carro1.acelerar()
carro2.acelerar()
carro2.frear()

# encapsulamento

class ContaBancaria:
    def __init__(self, titular,saldo): 
        self.titular = titular
        self.__saldo = saldo #atributo privado 

    def depositar(self,valor):
        self.__saldo += valor
    
    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else: 
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")


# herança
        
class Pessoa: 
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        super().__init(nome,idade)
        self.matricula = matricula

aluno1 = Aluno("Maria",20,"A123")
print(aluno1.nome)
print(aluno1.matricula)


# polimorfismo 

class Animal:
    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

animais = [Cachorro(), Gato(), Animal()]

for a in animais:
    a.emitir_som()

