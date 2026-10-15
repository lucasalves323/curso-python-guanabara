class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    #Métodos acessores
    def get_nota(self): #Método Getter (Pega a nota)
        return self._nota

    def set_nota(self, valor): #Método Setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida!')