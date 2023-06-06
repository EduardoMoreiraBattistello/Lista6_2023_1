class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print("Assinatura Simples: Acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium: Acesso a filmes e séries em qualidade HD e Ultra HD.")

# Criando instâncias das assinaturas
assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

# Criando array de assinaturas
assinaturas = [assinatura_simples, assinatura_premium]

# Percorrendo as assinaturas e exibindo os detalhes
for assinatura in assinaturas:
    print("Tipo de assinatura:", type(assinatura).__name__)
    print("Preço:", assinatura.calcular_preco())
    assinatura.exibir_detalhes()
    print()
