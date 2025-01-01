class B:
    vc = 123

    def __init__(self):
        pass

a1 = B()
a2 = B()

B.vc = "Alterado"

print(a1.vc) # variavel de instancia
print(a2.vc)
print(B.vc) # variavel da classe