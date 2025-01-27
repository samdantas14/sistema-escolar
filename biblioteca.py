from livro import Livro
class Biblioteca:
    def __init__(self):
        self._livros = []

    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self._livros.append(livro)
        else:
            raise TypeError("Apenas objetos do tipo 'Livro' podem ser adicionados à biblioteca.")

    def listar_livros(self):
        return [livro.apresentar() for livro in self._livros]

    def buscar_livro_por_titulo(self, titulo):
        for livro in self._livros:
            if livro.titulo == titulo:
                return livro.apresentar()
            else:
                return "Livro não encontrado na biblioteca."

    def total_livros(self):
        return len(self._livros)
