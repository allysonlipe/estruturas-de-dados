from No import No


class ListaEncadeada:
    def __init__(self):
        self.__inicio = None

    def is_vazia(self):
        return self.__inicio is None

    def tamanho(self):
        qtd = 0
        no = self.__inicio
        while (no != None):
            qtd = qtd + 1
            no = no.prox
        return qtd

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        novo_no.prox = self.__inicio
        self.__inicio = novo_no

    def inserir_final(self, valor):
        novo_no = No(valor)
        if (self.__inicio == None):
            self.__inicio = novo_no
        else:
            atual = self.__inicio
            while (atual.prox != None):
                atual = atual.prox
            atual.prox = novo_no

    def remover_inicio(self):
        if (self.__inicio == None):
            return None
        valor = self.__inicio.valor
        self.__inicio = self.__inicio.prox
        return valor

    def remover_final(self):
        if (self.__inicio == None):
            return False

        ant = None
        atual = self.__inicio
        while (atual.prox != None):
            ant = atual
            atual = atual.prox

        valor = atual.valor

        if (atual == self.__inicio):
            self.__inicio = atual.prox
        else:
            ant.prox = atual.prox

        return valor

    def remover_valor(self, valor):
        if (self.__inicio == None):
            return None

        ant = None
        atual = self.__inicio
        while (atual != None and atual.valor != valor):
            ant = atual
            atual = atual.prox

        if (atual == None):
            return None

        if (atual == self.__inicio):
            self.__inicio = atual.prox
        else:
            ant.prox = atual.prox

        return atual.valor

    def imprimir(self):
        qtd = 0
        atual = self.__inicio
        while (atual != None):
            print(atual.valor, end=' -> ')
            qtd = qtd + 1
            atual = atual.prox
        print("None")
