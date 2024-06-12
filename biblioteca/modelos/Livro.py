class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano}) [{self.genero}]"