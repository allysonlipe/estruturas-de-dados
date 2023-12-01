from No import No


class PilhaEncadeada:
    def __init__(self):
        self.__topo = None

    def is_vazia(self):
        return self.__topo is None

    def tamanho(self):
        qtd = 0
        no = self.__topo
        while (no != None):
            qtd = qtd + 1
            no = no.prox
        return qtd

    def push(self, valor):
        novo_no = No(valor)
        novo_no.prox = self.__topo
        self.__topo = novo_no

    def pop(self):
        if (self.is_vazia()):
            return None
        valor = self.__topo.valor
        self.__topo = self.__topo.prox
        return valor

    def get_posicao(self, valor):
        if (self.__topo == None):
            return None

        posicao = 0
        atual = self.__topo
        while (atual != None and atual.valor != valor):
            posicao += 1
            atual = atual.prox

        return posicao

    def get_topo(self):
        return self.__topo.valor

    def imprimir(self):
        qtd = 0
        atual = self.__topo
        while (atual != None):
            print(atual.valor, '\n')
            qtd = qtd + 1
            atual = atual.prox
        print("None")
