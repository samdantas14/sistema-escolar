from pessoa import Pessoa
from aluno import Aluno
from turma import Turma
from Escola1  import escola
from funcionario import Funcionario
from livro import Livro
from biblioteca import Biblioteca
from professor import Professor
from coordenador import Coordenador

Escola = escola("IFRN campus Pau dos Ferros", "Rua Julio Curioso, 22")


aluno1 = Aluno("Paulin", 18, "20231094010045", "2º Infomat")
aluno2 = Aluno("Madson", 17, "20221091010018", "3º Apivesp")
aluno3 = Aluno('teo',22,'23049382', '2º infomat')
professor = Professor("luix", 38, "Eletricidade")
funcionario = Funcionario("Zuilma", 60, "Dona da cantina")
coordenador = Coordenador("Ciro", 34, "PEOO", "Coordenação do curso de Informática")


Escola.adicionar_pessoa(aluno1)
Escola.adicionar_pessoa(aluno2)
Escola.adicionar_pessoa(aluno3)
Escola.adicionar_pessoa(professor)
Escola.adicionar_pessoa(funcionario)
Escola.adicionar_pessoa(coordenador)


turma1 = Turma('2º Infomat', 2023)
turma2 = Turma("3º Apivesp", 2022)
turma1.adicionar_aluno(aluno1)
turma2.adicionar_aluno(aluno2)
turma1.adicionar_aluno(aluno3)


biblioteca = Biblioteca()
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("O Extraordinário", "R. J. Palacio", 2012)
livro3 = Livro("Linhas e Rimas", "Maria Clara Machado", 1980)
livro4 = Livro("O segredo do juros", "tio tiago", 2006)
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
biblioteca.adicionar_livro(livro4)


print("=== Pessoas na Escola ===")
print("\n".join(Escola.listar_pessoas()))
print(f"Total de pessoas na escola: {Escola.total_pessoas()}\n")

print("=== Turma 2º Infomat ===")
print("\n".join(turma1.listar_alunos()))
print(f"Total de alunos na turma 2º Infomat: {turma1.total_alunos()}\n")

print("=== Turma 3º Apivesp ===")
print("\n".join(turma2.listar_alunos()))
print(f"Total de alunos na turma 3º Apivesp: {turma2.total_alunos()}\n")

print("=== Biblioteca ===")
print("\n".join(biblioteca.listar_livros()))
print(f"Total de livros na biblioteca: {biblioteca.total_livros()}\n")


print("=== Ações ===")
print(aluno1.estudar("Inglês"))
print(professor.dar_aula())
print(funcionario.trabalhar())
print(coordenador.coordenar())
print(coordenador.apresentar())


print("=== Buscas ===")
print(Escola.buscar_pessoa_por_nome("Ciro"))
print(turma1.buscar_aluno_por_nome("Paulin"))
print(biblioteca.buscar_livro_por_titulo("o segredo do juros"))


print("=== Atualizações ===")
print(aluno1.envelhecer(1)) 
print(livro1.atualizar_ano(2025))  
