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

with open("transacoes.csv", "w", newline="", encoding="utf-8") as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow(["Data", "Descricao", "Tipo", "Valor"])

    data_inicial = datetime.now()

    for i in range(10):

        data = data_inicial + timedelta(days=i)
        descricao = random.choice(descricoes)
        tipo = random.choice(tipos)
        valor = round(random.uniform(10, 500), 2)

        escritor.writerow([
            data.strftime("%d/%m/%Y"),
            descricao,
            tipo,
            valor
        ])

print("10 transações foram geradas com sucesso!")