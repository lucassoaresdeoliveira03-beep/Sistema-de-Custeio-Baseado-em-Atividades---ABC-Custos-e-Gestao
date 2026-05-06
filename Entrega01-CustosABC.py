# ============================================
# SISTEMA ABC - PRIMEIRA ENTREGA
# ============================================
 
def linha():
    print("*" * 30)
def nome_produto(nome):
    print(f'\n{nome}\n')
def linha_grande():
    print('\n')
    print('*'* 100)
# CADASTRO DE PRODUTOS

linha()
print('=== CADASTRE SEUS PRODUTOS ===')
linha()

# CADASTRO PRODUTO 1

nome_produto('CADASTRO DO PRIMEIRO PRODUTO')

nome_produto_1 = input(f"Digite o nome do primeiro produto --> ")
quantidade_produto_1 = float(input(f"Digite a quantidade de {nome_produto_1}s --> "))
custo_direto_produto_1 = float(input(f"Digite o custo direto de {nome_produto_1}s --> "))

# CADASTRO PRODUTO 2

nome_produto('CADASTRO DO SEGUNDO PRODUTO')

nome_produto_2 = input(f"Digite o nome do segundo produto --> ")
quantidade_produto_2 = float(input(f"Digite a quantidade de {nome_produto_2}s --> "))
custo_direto_produto_2 = float(input(f"Digite o custo direto de {nome_produto_2}s --> "))

# CADASTRO DE ATIVIDADES

linha_grande()

print('\n')
linha()
print('== CADASTRE SUAS ATIVIDADES ==')
linha()

# CADASTRO ATIVIDADE 1

nome_produto("CADASTRO DA PRIMEIRA ATIVIDADE")

nome_atividade_1 = input(f'Digite o nome da primeira atividade --> ')
custo_atividade_1 = float(input(f'Digite o custo de {nome_atividade_1} --> '))

# CADASTRO ATIVIDADE 2

nome_produto("CADASTRO DA SEGUNDA ATIVIDADE")

nome_atividade_2 = input(f'Digite o nome da segunda atividade --> ')
custo_atividade_2 = float(input(f'Digite o custo de {nome_atividade_2} --> '))

# CADASTRO CONSUMO DAS ATIVIDADES
linha_grande()

print('\n')
linha()
print('=== CONSUMO DAS ATIVIDADES ===')
linha()

# CONSUMO PRODUTO 1

print(f'\n{nome_produto_1}: ')
consumo_do_prod1_atividade1 = float(input(f'Consumo de {nome_atividade_1} --> '))
consumo_do_prod1_atividade2 = float(input(f'Consumo de {nome_atividade_2} --> '))

# CONSUMO PRODUTO 2

print(f'\n{nome_produto_2}: ')
consumo_do_prod2_atividade1 = float(input(f'Consumo de {nome_atividade_1} --> '))
consumo_do_prod2_atividade2 = float(input(f'Consumo de {nome_atividade_2} --> '))