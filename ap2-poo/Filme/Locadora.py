from datetime import datetime, timedelta
class Filme:
    class FilmeError(Exception):
        pass
    class FilmeIndisponivelError(FilmeError):
        pass

    def __init__(self, titulo, diretor, ano, ):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.disponivel = True
        self.data_aluguel = None

    def alugar(self):
        if not self.disponivel:
            raise Filme.FilmeIndisponivelError(f"O filme '{self.titulo}' não está disponível para aluguel.")
        self.disponivel = False
        self.data_aluguel = datetime.now()
    
    def devolver(self):
        if self.disponivel:
            raise Filme.FilmeError(f"O filme '{self.titulo}' não está alugado.")
        self.disponivel = True
        self.data_aluguel = None
        return self.calcular_multa()
    
    def calcular_multa(self):
        if self.data_aluguel:
            dias_aluguel = (datetime.now() - self.data_aluguel).days
            if dias_aluguel > 14:
                return (dias_aluguel - 14) * 2.5
        return 0
    
    def __str__(self):
        status = "Disponível" if self.disponivel else "Alugado"
        return f"'{self.titulo}' dirigido por {self.diretor} ({self.ano}) - Status: {status}"

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
    

if __name__ == "__main__":
    filme1 = Filme("Inception", "Christopher Nolan", 2010)
    filme2 = Filme("The Matrix", "The Wachowskis", 1999)

    usuario = Usuario("Alice", 1)
    usuario2 = Usuario("Bob", 2)

    print(usuario)
    print(usuario2)
    print(filme1)
    print(filme2)

    try:
        usuario.alugar_filme(filme1)
        print(f"Filme alugado: {filme1}")
    except Usuario.UsuarioError as e:
        print(e)
    try:
        usuario2.alugar_filme(filme2)   
    except Usuario.UsuarioError as e:
        print(e)
    print(usuario.listar_filmes_alugados())
    print(usuario2.listar_filmes_alugados())

    # Simular devolução após 16 dias para testar multa
    filme1.data_aluguel -= timedelta(days=16)
    multa = usuario.devolver_filme(filme1)
    print(f"Filme devolvido: {filme1}, Multa: R${multa:.2f}")

    print(usuario)
    print(usuario2)

        