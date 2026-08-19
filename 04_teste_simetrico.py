import csv
from datetime import datetime, timedelta

arquivo_teste = "teste_simetrico.csv"

data_inicial = datetime(2026, 8, 19)

# Cria o arquivo de teste
with open(arquivo_teste, "w", newline="", encoding="utf-8") as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow(["Data", "Descricao", "Tipo", "Valor"])

    for i in range(4):

        data = data_inicial + timedelta(days=i)

        escritor.writerow([
            data.strftime("%d/%m/%Y"),
            "Credito Teste",
            "C",
            "100.00"
        ])

        escritor.writerow([
            data.strftime("%d/%m/%Y"),
            "Debito Teste",
            "D",
            "100.00"
        ])


# Lê o arquivo e calcula os saldos
saldos = {}

with open(arquivo_teste, "r", newline="", encoding="utf-8") as arquivo:

    leitor = csv.DictReader(arquivo)

    for transacao in leitor:

        data = transacao["Data"]
        tipo = transacao["Tipo"]
        valor = float(transacao["Valor"])

        if data not in saldos:
            saldos[data] = 0.0

        if tipo == "C":
            saldos[data] += valor

        elif tipo == "D":
            saldos[data] -= valor


# Verifica se todos os saldos são exatamente 0.00
print("===== TESTE SIMÉTRICO =====")

teste_aprovado = True

for data, saldo in saldos.items():

    print(f"{data} → Saldo: R$ {saldo:.2f}")

    if saldo != 0.0:
        teste_aprovado = False


if teste_aprovado:
    print("\nTESTE APROVADO!")
else:
    print("\nTESTE REPROVADO!")