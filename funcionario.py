from pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, idade, funcao):
        super().__init__(nome, idade)
        self._funcao = funcao

    def apresentar(self):
        return f"Sou o funcionário {self._nome}, responsável por {self._funcao}."
    
    def trabalhar(self):
        return f"{self._nome} está desempenhando a função de {self._funcao}."
