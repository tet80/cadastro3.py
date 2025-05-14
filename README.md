Cadastro de Produtos em Python
Este é um sistema simples em Python para cadastro e listagem de produtos, utilizando listas para armazenar os dados.

Funcionalidades
Cadastrar Produto: Permite ao usuário cadastrar novos produtos fornecendo nome, descrição, valor e disponibilidade para venda.

Listagem de Produtos: Exibe todos os produtos cadastrados ordenados por valor.

Persistência de Dados: Os produtos são armazenados em uma lista durante a execução do programa.

Requisitos
Python 3.x instalado


Estrutura do Projeto
main.py: Contém o código principal do programa.

Exemplo de Código
python
Copiar
Editar
class Produto:
    def __init__(self, nome, descricao, valor, disponivel):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.disponivel = disponivel

    def __repr__(self):
        return f"{self.nome} - R${self.valor:.2f}"

produtos = []

def cadastrar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição: ")
    valor = float(input("Valor: R$"))
    disponivel = input("Disponível para venda (s/n): ").lower() == 's'
    produto = Produto(nome, descricao, valor, disponivel)
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    if produtos:
        print("\nProdutos cadastrados:")
        for produto in produtos:
            print(produto)
    else:
        print("Nenhum produto cadastrado.")

def menu():
    while True:
        print("\n1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para sugerir melhorias ou enviar pull requests.

