import csv
import random
from datetime import datetime, timedelta

descricoes = [
    "Mercado",
    "Uber",
    "Salário",
    "Farmácia",
    "Restaurante"
]

tipos = ["C", "D"]

descricao = random.choice(descricoes)
tipo = random.choice(tipos)
valor = random.uniform(10, 500)
data = datetime.now()

with open("transacoes.csv", "w", newline="") as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow(["Data", "Descricao", "Tipo", "Valor"])

    escritor.writerow([data, descricao, tipo, valor])