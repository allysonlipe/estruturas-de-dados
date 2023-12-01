from No import No


class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def is_vazia(self):
        return self.__inicio is None

    def tamanho(self):
        qtd = 0
        no = self.__inicio
        while (no != None):
            qtd = qtd + 1
            no = no.prox
        return qtd

    def inserir(self, valor):
        novo_no = No(valor)
        if (self.is_vazia()):
            self.__inicio = novo_no
        else:
            self.__fim.prox = novo_no
        self.__fim = novo_no

    def remover(self):
        if (self.is_vazia()):
            return None
        valor = self.__inicio.valor
        if (self.__inicio == self.__fim):
            self.__inicio = None
            self.__final = None
            return valor
        self.__inicio = self.__inicio.prox
        return valor

    def imprimir(self):
        qtd = 0
        atual = self.__inicio
        while (atual != None):
            print(atual.valor, end=' -> ')
            qtd = qtd + 1
            atual = atual.prox
        print("None")

    def get_inicio(self):
        return self.__inicio.valor

    def get_fim(self):
        return self.__fim.valor
