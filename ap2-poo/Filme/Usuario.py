from datetime import datetime, timedelta
from Filme import Filme

class Usuario:
    class UsuarioError(Exception):
        pass

    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.filmes_alugados = []

    def alugar_filme(self, filme:Filme):
        try:
            filme.alugar()
            self.filmes_alugados.append(filme)
        except Filme.FilmeIndisponivelError as e:
            raise Usuario.UsuarioError(str(e))

    def devolver_filme(self, filme:Filme):
        if filme not in self.filmes_alugados:
            raise Usuario.UsuarioError(f"O usuário '{self.nome}' não alugou o filme '{filme.titulo}'.")
        multa = filme.devolver()
        self.filmes_alugados.remove(filme)
        return multa

    def listar_filmes_alugados(self):
        return [str(filme) for filme in self.filmes_alugados]
    
    def __str__(self):
        return f"Usuário: {self.nome} (ID: {self.id_usuario}) - Filmes alugados: {len(self.filmes_alugados)}"
    