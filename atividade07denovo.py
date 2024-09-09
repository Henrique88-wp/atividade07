# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.

valor_produto = float(input("digite o preço do produto"))
taxa = 0.12
r = valor_produto+(valor_produto*taxa)
print(f"seu produto final é de {r}")