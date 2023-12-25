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
                    print("=======================")
                    print("Matrícula já cadastrada!!")
                    print("=======================")
                    return False  # elemento já existe

                if (aluno.matricula > atual.aluno.matricula):
                    atual = atual.dir

                else:
                    atual = atual.esq

            if (aluno.matricula > ant.aluno.matricula):
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
            if (matricula == atual.aluno.matricula):
                print("Aluno encontrado!!!")
                print(f"Nome: {atual.aluno.nome}")
                print(f"Matrícula: {atual.aluno.matricula}")
                print(f"Nota 1: {atual.aluno.nota1}")
                print(f"Nota 2: {atual.aluno.nota2}")
                print(f"Média: {atual.aluno.media}")
                return True

            if (matricula > atual.aluno.matricula):
                atual = atual.dir
            else:
                atual = atual.esq

        print("Aluno não encontrado!")
        return False

    def __listar(self, no):
        if (no != None):
            self.__listar(no.esq)
            print(f"Nome: {no.aluno.nome}")
            print(f"Matrícula: {no.aluno.matricula}")
            print(f"Nota 1: {no.aluno.nota1}")
            print(f"Nota 2: {no.aluno.nota2}")
            print(f"Média: {no.aluno.media}")
            self.__listar(no.dir)

    def listar_alunos(self):
        if (self.vazia()):
            print("A lista está vazia!!!!")
        else:
            print("Listagem de alunos:")
            self.__listar(self.__raiz)

    def remover(self, matricula):
        if (self.__raiz == None):
            print("Não é possível remover pois a estrutura está vazia.")
            return False

        ant = None
        atual = self.__raiz
        while atual != None:
            if (matricula == atual.aluno.matricula):
                if (atual == self.__raiz):
                    self.__raiz = self.__remove_atual(atual)
                else:
                    if (ant.dir == atual):
                        ant.dir = self.__remove_atual(atual)
                    else:
                        ant.esq = self.__remove_atual(atual)
                return True

            ant = atual
            if (matricula > atual.aluno.matricula):
                atual = atual.dir
            else:
                atual = atual.esq
        print("Matricula não encontrada!!!!")
        return False

    def __remove_atual(self, atual):
        if (atual.esq == None):
            return atual.dir

        no1 = atual
        no2 = atual.esq
        while (no2.dir != None):
            no1 = no2
            no2 = no2.dir

        if (no1 != atual):
            no1.dir = no2.esq
            no2.esqp = atual.esq

        no2.dir = atual.dir
        return no2

    def inserirNota(self, matricula):
        if (self.vazia()):
            print("A lista está vazia!!!!")
        else:
            atual = self.__raiz
            while atual != None:
                if (matricula == atual.aluno.matricula):
                    print("Aluno encontrado!!!")
                    print(f"Nome: {atual.aluno.nome}")
                    print(f"Matrícula: {atual.aluno.matricula}")
                    controle = input(
                        "Você deseja alterar a nota1 ou a nota2?(Responda com 1 ou 2) ")
                    while (controle != "1" or controle != "2"):
                        if (controle == "1"):
                            atual.aluno.nota1 = float(input("Digite a nota1:"))
                            print(f"Nota1 alterada com sucesso para: {atual.aluno.nota1}")
                            return
                        if (controle == "2"):
                            atual.aluno.nota2 = float(input("Digite a nota2:"))
                            print(f"Nota2 alterada com sucesso para: {atual.aluno.nota2}")
                            return
                        else:
                            print("Digite uma opção válida!!!")

                    return True

                if (matricula > atual.aluno.matricula):
                    atual = atual.dir
                else:
                    atual = atual.esq

            print("Matrícula não encontrada!!")
            return False
        
    def media(self, matricula):
        if (self.vazia()):
            print("A lista está vazia!!!!")
        else:
            atual = self.__raiz
            while atual != None:
                if (matricula == atual.aluno.matricula):
                    print("Aluno encontrado!!!")
                    print(f"Nome: {atual.aluno.nome}")
                    print(f"Matrícula: {atual.aluno.matricula}")
                    if(atual.aluno.nota1 != None and atual.aluno.nota2 != None):
                        atual.aluno.media = (atual.aluno.nota1 + atual.aluno.nota2)/2
                        print(f"A média do aluno é {atual.aluno.media}")
                    else:
                        print("ERRO!!!!!!")
                        print("Atenção, preencha as notas do aluno primeiro!!!")

                    return True

                if (matricula > atual.aluno.matricula):
                    atual = atual.dir
                else:
                    atual = atual.esq

            print("Matrícula não encontrada!!")
            return False

    