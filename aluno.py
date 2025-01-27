from pessoa import Pessoa
class Aluno(Pessoa):
    
    def __init__(self, nome, idade, matricula, turma):
        super().__init__(nome, idade)
        self._matricula = matricula
        self._turma = turma

    def apresentar(self):
        return f"Sou o aluno {self._nome}, da turma {self._turma}."
    
    def estudar(self, materia):
        return f"{self._nome} está estudando {materia}."

