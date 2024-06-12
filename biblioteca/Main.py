from modelos.Livro import Livro
from estruturas.BinaryTree import BinaryTree
from estruturas.ListaDuplamenteLigada import ListaDuplamenteLigada
from estruturas.Pilha import Pilha
from utils.LimparTela import limpar_tela

class BibliotecaConsole:
    def __init__(self):
        self.arvore = BinaryTree()
        self.lista = ListaDuplamenteLigada()
        self.historico_undo = Pilha()

    def validar_entrada(self, prompt, tipo):
        while True:
            entrada = input(prompt)
            try:
                if tipo == 'int':
                    return int(entrada)
                elif tipo == 'str':
                    return entrada.strip()
            except ValueError:
                print(f"Entrada inválida. Por favor, insira um {tipo} válido.")

    def adicionar_livro(self):
        titulo = self.validar_entrada("Título: ", 'str')
        autor = self.validar_entrada("Autor: ", 'str')
        ano = self.validar_entrada("Ano: ", 'int')
        genero = self.validar_entrada("Gênero: ", 'str')
        livro = Livro(titulo, autor, ano, genero)

        if self.arvore.search(titulo):
            print(f"Livro com título '{titulo}' já existe.")
            return
        
        self.arvore.insert(titulo)
        self.lista.append(livro)
        self.historico_undo.push(('add', livro))
        print(f"Livro '{titulo}' adicionado com sucesso!")

    def remover_livro(self):
        titulo = self.validar_entrada("Título do livro a ser removido: ", 'str').lower()
        atual = self.lista.head
        while atual:
            if atual.value.titulo.lower() == titulo:
                livro_removido = atual.value
                self.lista.remove(atual.value)
                self.arvore.remove(titulo)
                self.historico_undo.push(('remove', atual.value))
                print(f"Livro '{livro_removido.titulo}' removido com sucesso.")
                return  
            atual = atual.next
        print(f"Livro '{titulo}' não encontrado.")

    def buscar_livro(self):
        titulo = self.validar_entrada("Título do livro a ser buscado: ", 'str')
        atual = self.lista.head
        while atual:
            if atual.value.titulo == titulo:
                livro_encontrado = atual.value
                print(f"Livro encontrado: {livro_encontrado.titulo} - {livro_encontrado.autor} ({livro_encontrado.ano}) [{livro_encontrado.genero}]")
                return
            atual = atual.next
        print(f"Livro '{titulo}' não encontrado.")

    def ordenar_livros(self):
        print("Livros ordenados:")
        self.arvore.inorder(self._print_livro)

    def _print_livro(self, titulo):
        atual = self.lista.head
        while atual:
            if atual.value.titulo == titulo:
                livro = atual.value
                print(f"{livro.titulo} - {livro.autor} ({livro.ano}) [{livro.genero}]")
                break
            atual = atual.next

    def desfazer_acao(self):
        if self.historico_undo.is_empty():
            print("Nada para desfazer.")
            return
        acao, livro = self.historico_undo.pop()
        if acao == 'add':
            if self.lista.remove(livro):
                self.arvore.remove(livro.titulo)
                print(f"Ação desfeita: Adição do livro '{livro.titulo}'")
            else:
                print(f"Erro ao desfazer: O livro '{livro.titulo}' não foi encontrado na lista.")
        elif acao == 'remove':
            self.lista.append(livro)
            self.arvore.insert(livro.titulo)
            print(f"Ação desfeita: Remoção do livro '{livro.titulo}'")

    def exibir_menu(self):
        while True:
            limpar_tela()
            print("\nBiblioteca de Livros Inteligente")
            print("1. Adicionar Livro")
            print("2. Remover Livro")
            print("3. Buscar Livro")
            print("4. Ordenar Livros")
            print("5. Desfazer Ação")
            print("6. Sair")
            opcao = self.validar_entrada("Escolha uma opção: ", 'str')
            if opcao == '1':
                self.adicionar_livro()
            elif opcao == '2':
                self.remover_livro()
            elif opcao == '3':
                self.buscar_livro()
            elif opcao == '4':
                self.ordenar_livros()
            elif opcao == '5':
                self.desfazer_acao()
            elif opcao == '6':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    biblioteca = BibliotecaConsole()
    biblioteca.exibir_menu()
