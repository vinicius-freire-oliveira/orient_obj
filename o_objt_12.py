# Encapsulamento
# Comentário explicando a finalidade do código
# Definição da classe Pessoa para representar informações sobre pessoas

class Pessoa():
    def __init__(self, nome, idade):
        # Inicialização dos atributos da instância como atributos privados com o prefixo '__'
        self.__nome = nome
        self.__idade = idade

    # Método para obter o valor do atributo privado '__nome'
    def getNome(self):
        return self.__nome

    # Método para obter o valor do atributo privado '__idade'
    def getIdade(self):
        return self.__idade

    # Método para modificar o valor do atributo privado '__nome'
    def setNome(self, nome):
        self.__nome = nome

    # Método para modificar o valor do atributo privado '__idade'
    def setIdade(self, idade):
        self.__idade = idade

    # Método para imprimir as informações da pessoa
    def imprimir(self):
        print(f"Meu nome é {self.getNome()} e tenho {self.getIdade()} anos")

# Criação de uma instância da classe Pessoa com nome "Abdias de Carvalho" e idade 65
pessoa = Pessoa("Abdias de Carvalho", 65) 
# Chama o método imprimir() para imprimir as informações da pessoa
pessoa.imprimir()

# Modificação do nome e idade da pessoa usando os métodos setters
pessoa.setNome("Caetano Veloso")
pessoa.setIdade(80)
# Chama o método imprimir() novamente para imprimir as novas informações da pessoa
pessoa.imprimir()
