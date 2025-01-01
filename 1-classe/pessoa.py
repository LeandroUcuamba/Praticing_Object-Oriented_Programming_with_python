class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.falando = falando


    def comer(self, alimento):
        if self.comendo:
            print(f'O {self.nome} já está comendo!!!')
        else:
            print(f'O {self.nome} está comendo {alimento}')
            self.comendo = True