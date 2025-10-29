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