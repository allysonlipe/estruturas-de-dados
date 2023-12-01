class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserirInicio(self, valor):
        novoNo = No(valor)
        if (self.inicio == None):
            self.inicio = self.fim = novoNo
        else:
            novoNo.proximo = self.inicio
            novoNo.anterior = None
            self.inicio.anterior = novoNo
            self.inicio = novoNo

    def inserirFim(self, valor):
        novoNo = No(valor)
        novoNo.proximo = None
        if self.fim == None:
            self.inicio = novoNo
            self.fim = novoNo
        else:
            self.fim.proximo = novoNo
            novoNo.anterior = self.fim
            self.fim = novoNo

    def mostrarLista(self):
        atual = self.inicio
        if (self.inicio == None):
            print("Lista Vazia.")
        else:
            while (atual != None):
                print(atual.valor)
                atual = atual.proximo

    def removerInicio(self):
        if (self.inicio == None):
            print("A lista está vazia, não é possível remover.")
            return

        atual = self.inicio

        if (self.inicio.proximo != None):
            self.inicio = atual.proximo
            self.inicio.anterior = None
        else:
            self.inicio = None
            self.fim = None

        atual = None

    def removerFim(self):
        if (self.inicio == None):
            print("A lista está vazia, não é possível remover.")

        atual = self.fim

        if (self.fim != None):
            self.fim = atual.anterior
            self.fim.proximo = None
        else:
            self.inicio = None
            self.fim = None

        atual = None


    def removerPorValor(self, valor):
        if self.inicio is None:
            print("A lista está vazia, não é possível remover.")
            return

        atual = self.inicio

        while atual is not None:
            if atual.valor == valor:
                if atual == self.inicio:
                    self.removerInicio()
                    return
                elif atual == self.fim:
                    self.removerFim()
                    return
                else:
                    anterior = atual.anterior
                    proximo = atual.proximo

                    anterior.proximo = proximo
                    proximo.anterior = anterior
                    return

            atual = atual.proximo
            if(atual == None):
                print("Não encontrei o elemento na lista.")
                return 


# MANIPULAÇÃO ===========================================

minhaLista = ListaDupla()
minhaLista.inserirInicio(1)
minhaLista.inserirInicio(2)
minhaLista.inserirInicio(3)
minhaLista.inserirInicio(4)
minhaLista.inserirFim(5)
minhaLista.mostrarLista()
print("=================")
minhaLista.removerPorValor(3)
minhaLista.mostrarLista()