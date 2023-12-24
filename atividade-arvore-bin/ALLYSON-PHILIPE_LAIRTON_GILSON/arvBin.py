from no import No


class ArvBin:
    def __init__(self):
        self.__raiz = None

    def vazia(self):
        if (self.__raiz == None):
            return True
        else:
            return False

    def totalNO(self):
        if (self.__raiz == None):
            return 0
        else:
            return self._totalNO(self.__raiz)

    def _totalNO(self, raiz):
        if (raiz == None):
            return 0

        total_esq = self._totalNO(raiz.esq)
        total_dir = self._totalNO(raiz.dir)
        return (total_esq + total_dir + 1)

    def inserir(self, aluno):
        novo = No(aluno)
        
        if (self.__raiz == None):
            self.__raiz = novo
        else:
            atual = self.__raiz
            ant = None
            while (atual != None):
                ant = atual
                if (aluno.matricula == atual.aluno.matricula):
                    return False  # elemento já existe

                if (aluno.matricula > atual.aluno.matricula):
                    atual = atual.dir

                else:
                    atual = atual.esq

            if (aluno.matricula > ant.matricula):
                ant.dir = novo
            else:
                ant.esq = novo
        return True

    def busca(self, matricula):
        if self.__raiz == None:
            print("Árvore vazia - Aluno não encontrado")
            return False

        atual = self.__raiz
        while atual != None:
            if matricula == atual.aluno.matricula:
                print("Aluno encontrado!!!")
                print(f"Nome: {atual.aluno.nome}")
                print(f"Matrícula: {atual.aluno.matricula}")
                print(f"Nota 1: {atual.aluno.nota1}")
                print(f"Nota 2: {atual.aluno.nota2}")
                print(f"Média: {atual.aluno.media}")
                return True

            if matricula > atual.aluno.matricula:
                atual = atual.dir
            else:
                atual = atual.esq

        print("Aluno não encontrado!")
        return False