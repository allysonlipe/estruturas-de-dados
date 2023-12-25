import os
from aluno import Aluno
# from No import No
from arvBin import ArvBin

arvore = ArvBin()


def limpar_console():
    os.system("cls")


loop = True
while loop == True:
    print("==========================================")
    print("============= MENU PRINCIPAL =============")
    print("==========================================")
    print("1. Adicionar um aluno")
    print("2. Listar todos os alunos")
    print("3. Remover aluno pela matrícula")
    print("4. Buscar aluno pela matrícula")
    print("5. Total de alunos cadastrados")
    print("6. Cadastrar notas de um aluno")
    print("7. Calcular média de um aluno")
    print("0. Sair")
    valor = input("Digite uma opção: ")
    

    if valor == "0":
        print(f"Opção escolhida: {valor}. Sair")
        print("Obrigado por utilizar nossos serviços.")
        loop = False

    if valor == "1":
        limpar_console()
        print(f"Opção escolhida: {valor}- Adicionar um aluno")
        matricula = input("Digite a matrícula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        novo_aluno = Aluno(nome, matricula)
        arvore.inserir(novo_aluno)
        

    if valor == "2":
        limpar_console()
        print(f"Opção escolhida: {valor}- Listar Alunos")
        arvore.listar_alunos()        
        

    if valor == "3":
        limpar_console()
        print(f"Opção escolhida: {valor}- Remover Aluno pela matrícula")
        matricula = input("Digite a matrícula que deseja remover: ")
        arvore.remover(matricula)
        

    if valor == "4":
        limpar_console()
        print(f"Opção escolhida: {valor}- Buscar aluno pela matrícula")
        matricula = input("Digite a matrícula que deseja pesquisar: ")
        limpar_console()
        arvore.busca(matricula)

    if valor == "5":
        limpar_console()
        print(f"Opção escolhida: {valor}- Total de alunos")
        print(f"Total de alunos cadastrados: {arvore.totalNO()}")

    if valor == "6":
        limpar_console()
        print(f"Opção escolhida: {valor}- Cadastrar Notas de um aluno")
        matricula = input("Digite a matrícula do aluno que você deseja alterar a nota: ")
        arvore.inserirNota(matricula)

    if valor == "7":
        limpar_console()
        print(f"Opção escolhida: {valor}- Calcular a média")
        matricula = input("Digite a matrícula do aluno que você deseja calcular a média: ")
        arvore.media(matricula)
        
