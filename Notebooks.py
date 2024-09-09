

# função perguntar nome
nome = input("Qual o seu nome? ")  # Não é necessário converter para `str`, pois `input` já retorna uma string.
print(f"Olá, {nome}. Qual modelo deseja consultar?")
print("Temos Dell\nPositivo\nMacbook")

#pergunta ao usuario qual note ele deseja
notebook_escolhido = input("Qual notebook seria da sua preferência? ")  # Também não é necessário converter para `str`.

# dados sobre os notebooks
def dell():
    print(f"Olá, {nome}")
    print("Temos 5 laptops Dell em estoque")

def positivo():
    print(f"Olá, {nome}")
    print("Temos 23 laptops Positivo em estoque")

def macbook():
    print(f"Olá, {nome}")
    print("Infelizmente não temos nenhum MacBook em estoque")
    print("Assim que nosso estoque for refeito, entraremos em contato")

# Verifica o notebook escolhido e chama a função correspondente
if notebook_escolhido.lower() == "dell":
    dell()
elif notebook_escolhido.lower() == "positivo":
    positivo()
elif notebook_escolhido.lower() == "macbook":
    macbook()
else:
    print("Modelo não reconhecido.")

# Função adicional para dar boas-vindas ao cliente (parece ser um exemplo separado)
#def boas_vindas_cliente1():
#    nome = input("Qual seu nome? ")
#    print(f"Olá, {nome}")
#    print("Temos 5 laptops em estoque")

#boas_vindas_cliente1()  # Chamada da função adicional
