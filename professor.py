from pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    def apresentar(self):
        return f"Sou o professor {self._nome}, responsável por {self._disciplina}."
    
    def dar_aula(self):
        return f"O professor {self._nome} está dando aula de {self._disciplina}."