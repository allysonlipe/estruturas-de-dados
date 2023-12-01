from FilaEncadeada import FilaEncadeada
from No import No

# Criando uma instância da FilaEncadeada
fila = FilaEncadeada()

op = None

while (op != 0):
    print("\nMenu Fila:")
    print("1. Enfileirar")
    print("2. Desenfileirar")
    print("3. Ver início")
    print("4. Ver final")
    print("5. Ver fila")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = input("Digite o valor: ")
        fila.inserir(valor)
    elif escolha == "2":
        fila.remover()
    elif escolha == "3":
        print('Início da fila: ', fila.get_inicio())
    elif escolha == "4":
        print('Final da fila: ', fila.get_fim())
    elif escolha == "5":
        fila.imprimir()
    elif escolha == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
