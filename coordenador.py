from funcionario import Funcionario
from professor import Professor
from pessoa import Pessoa
class Coordenador(Professor, Funcionario):
    def __init__(self, nome, idade, disciplina, funcao):
        Pessoa.__init__(self, nome, idade)
        self._disciplina = disciplina
        self._funcao = funcao

    def apresentar(self):
        return f"Sou o coordenador {self._nome}, responsável por {self._funcao} e ensino {self._disciplina}."
    
    def coordenar(self):
        return f"O coordenador {self._nome} está organizando atividades relacionadas a {self._funcao}."