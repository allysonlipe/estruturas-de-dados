from PilhaEncadeada import PilhaEncadeada
from No import No

# Criando uma instância da PilhaEncadeada
pilha = PilhaEncadeada()

op = None

while (op != 0):
    print("\nMenu Pilha:")
    print("1. Push")
    print("2. Pop")
    print("3. Obter posição de elemento")
    print("4. Ver topo da pilha")
    print("5. Ver pilha")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = input("Digite o valor: ")
        pilha.push(valor)
    elif escolha == "2":
        pilha.pop()
    elif escolha == "3":
        valor = input("Digite o valor: ")
        print('Posição: ', pilha.get_posicao(valor))
    elif escolha == "4":
        print('Topo da pilha: ', pilha.get_topo())
    elif escolha == "5":
        pilha.imprimir()
    elif escolha == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
