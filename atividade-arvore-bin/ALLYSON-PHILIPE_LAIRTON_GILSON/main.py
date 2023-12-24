import os
from aluno import Aluno
# from No import No
from arvBin import ArvBin

arvore = ArvBin()


def limpar_console():
    os.system("cls")


loop = True
while loop == True:
    print("1. Adicionar um aluno")
    print("2. Listar todos os alunos")
    print("3. Remover aluno pela matrícula")
    print("4. Buscar aluno pela matrícula")
    print("5. Total de alunos cadastrados")
    print("6. Cadastrar notas de um aluno")
    print("7. Calcular média de um aluno")
    print("0. Sair")
    valor = input("Digite uma opção: ")
    limpar_console()

    if valor == "0":
        print(f"Opção escolhida: {valor}. Sair")
        print("Obrigado por utilizar nossos serviços.")
        loop = False

    if valor == "1":
        print(f"Opção escolhida: {valor}. Adicionar um aluno")
        matricula = input("Digite a matrícula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota 1 do aluno: "))
        nota2 = float(input("Digite a nota 2 do aluno: "))
        media = (nota1+nota2)/2
        novo_aluno = Aluno(nome, matricula, nota1, nota2, media)
        arvore.inserir(novo_aluno)

    if valor == "2":
        print(f"Opção escolhida: {valor}.")

    if valor == "3":
        print(f"Opção escolhida: {valor}. ")
        

    if valor == "4":
        print(f"Opção escolhida: {valor}. Buscar aluno pela matrícula")
        matricula = input("Digite a matrícula que deseja pesquisar: ")
        arvore.busca(matricula)

    if valor == "5":
        print(f"Opção escolhida: {valor}.")
        print(f"Total de alunos cadastrados: {arvore.totalNO()}")

    if valor == "6":
        print(f"Opção escolhida: {valor}.")

    if valor == "7":
        print(f"Opção escolhida: {valor}.")
