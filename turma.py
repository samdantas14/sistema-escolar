from aluno import Aluno
class Turma:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._alunos = []

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self._alunos.append(aluno)
        else:
            raise TypeError("Apenas objetos do tipo 'Aluno' podem ser adicionados à turma.")

    def listar_alunos(self):
        return [aluno.apresentar() for aluno in self._alunos]
    
    def buscar_aluno_por_nome(self, nome):
        for aluno in self._alunos:
            if aluno._nome == nome:
                return aluno.apresentar()
        return "Aluno não encontrado na turma."

    def total_alunos(self):
        return len(self._alunos)
