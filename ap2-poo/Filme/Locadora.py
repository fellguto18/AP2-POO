from datetime import datetime, timedelta
from Filme import Filme
from Usuario import Usuario

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

        