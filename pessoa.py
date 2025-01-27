class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def apresentar(self):
        return f"Meu nome é {self._nome} e tenho {self._idade} anos."
    
    def falar(self, mensagem):
        return f"{self._nome} está falando: {mensagem}"
    
    def envelhecer(self, anos):
        self._idade += anos
        return f"{self._nome} agora tem {self._idade} anos."
