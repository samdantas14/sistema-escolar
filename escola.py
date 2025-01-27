class Aluno:
    def __init__(self,nome,idade,matricula,data_nascimento,cpf):
        self.nome= nome
        self.idade= idade
        self.matricula= matricula
        self.data_nascimento = data_nascimento
        self.__cpf = cpf

    def getatributos(self):
        print(f'olá eu sou {self.nome} tenho {self.idade} de idade minha matrícula é {self.matricula} nasci em {self.data_nascimento} e o meu cpf é {self._cpf}')
    
    def falar(self):
        return f'{self.nome} está falando'
    
    def mudaCPF(self, cpf):
        if self.__validarCpf(cpf):
            self.__cpf = cpf
    
    def __validarCpf(self,cpf):
        if cpf == '123.456.789-00':
            return True
        else: 
            return False
    
class professor(Aluno):
    def __init__(self, nome, idade, matricula, data_nascimento, cpf,materias):
        super().__init__(nome, idade, matricula, data_nascimento, cpf)
        self.materias = materias

    def falar(self):
        return f'o professor {self.nome} está dizendo oi para a turma'

    def getDados(self):
        pass

    

