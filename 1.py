class UnidadeMilitar:
    def mover(self):
        print("A unidade está se movendo.")

    def atacar(self):
        print("A unidade está atacando.")

class Soldado(UnidadeMilitar):
    def mover(self):
        print("O soldado está marchando.")

    def atacar(self):
        print("O soldado está atirando.")

class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("O arqueiro está se deslocando.")

    def atacar(self):
        print("O arqueiro está disparando flechas.")

class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("O cavaleiro está galopando.")

    def atacar(self):
        print("O cavaleiro está empunhando sua espada.")

# Criando instâncias das unidades
unidades = [Soldado(), Arqueiro(), Cavaleiro()]

# Percorrendo as unidades e chamando os métodos mover() e atacar()
for unidade in unidades:
    unidade.mover()
    unidade.atacar()
