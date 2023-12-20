import os
from aluno import Aluno
# from No import No
# from AgendaTelefonica import AgendaTelefonica

# agenda=AgendaTelefonica()
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
    valor=input("Digite uma opção: ")
    limpar_console()
    
    if valor == "0":
        print(f"Opção escolhida: {valor}. Sair")
        print("Obrigado por utilizar nossos serviços.")
        loop = False