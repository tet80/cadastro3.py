# Inicializa listas para armazenar os nomes e idades
NOME = [''] * 3  # Lista para armazenar os nomes
IDADE = [0] * 3  # Lista para armazenar as idades
TELEFONE = [''] * 3  # Lista para armazenar os telefones
RUA = [''] * 3  # Lista para armazenar as ruas
NUMERO = [0] * 3  # Lista para armazenar os números das casas
BAIRRO = [''] * 3  # Lista para armazenar os bairros

# Laço para cadastro de 3 pessoas
for cont in range(3):
    print(f"-------------- {cont + 1}º - CADASTRO ------------")
    print()
    
    # Recebe o nome do usuário
    print("Digite o seu nome:")
    NOME[cont] = input()
    
    # Recebe a idade do usuário
    print("Digite a sua idade:")
    IDADE[cont] = int(input())
    
    # Recebe o telefone do usuário
    print("Digite o seu telefone (ex: 99999-9999):")
    TELEFONE[cont] = input()
    
    # Recebe a rua do usuário
    print("Digite a sua rua:")
    RUA[cont] = input()
    
    # Recebe o número da casa/apartamento
    print("Digite o número da sua casa/apartamento:")
    NUMERO[cont] = int(input())
    
    # Recebe o bairro do usuário
    print("Digite o seu bairro:")
    BAIRRO[cont] = input()

# Exibe os cadastros após o preenchimento
for cont in range(3):
    print(f"-------------------------")
    print(f"NOME: {NOME[cont]}")
    print(f"IDADE: {IDADE[cont]} anos")
    print(f"TELEFONE: {TELEFONE[cont]}")
    print(f"RUA: {RUA[cont]}")
    print(f"NÚMERO: {NUMERO[cont]}")
    print(f"BAIRRO: {BAIRRO[cont]}")
    print("-------------------------")
