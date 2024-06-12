import os

def limpar_tela():
    input("\nPressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')