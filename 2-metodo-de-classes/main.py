from pessoa import Pessoa

p1 = Pessoa.por_ano_nascimento('Leandro', 1999)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()