class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def apresentar(self):
        return f"O livro {self.titulo}, foi escrito por {self.autor} e publicado no ano {self.ano}."
    
    def atualizar_ano(self, novo_ano):
        self.ano = novo_ano
        return f"O ano do livro {self.titulo} foi atualizado para {self.ano}."
