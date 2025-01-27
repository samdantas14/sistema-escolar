from pessoa import Pessoa
class escola: 
    def __init__(self, nome, endereco):
        self._nome = nome  
        self._endereco = endereco 
        self._pessoas = [] 

    def adicionar_pessoa(self, pessoa):
        if isinstance(pessoa, Pessoa):
            self._pessoas.append(pessoa)
        else:
            raise TypeError("Apenas objetos do tipo 'Pessoa' podem ser adicionados à escola.")

    def listar_pessoas(self):
        return [pessoa.apresentar() for pessoa in self._pessoas]

    def buscar_pessoa_por_nome(self, nome):
        for pessoa in self._pessoas:
            if pessoa._nome == nome:
                return pessoa.apresentar()
        return "Pessoa não encontrada na escola."

    def total_pessoas(self):
        return len(self._pessoas)