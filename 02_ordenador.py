import csv

transacoes = []

with open("transacoes.csv", "r", newline="", encoding="utf-8") as arquivo:

    leitor = csv.DictReader(arquivo)

    for transacao in leitor:
        transacao["Valor"] = float(transacao["Valor"])
        transacoes.append(transacao)

transacoes.sort(key=lambda transacao: transacao["Tipo"])

with open("transacoes_ordenadas.csv", "w", newline="", encoding="utf-8") as arquivo:

    escritor = csv.DictWriter(
        arquivo,
        fieldnames=["Data", "Descricao", "Tipo", "Valor"]
    )

    escritor.writeheader()

    for transacao in transacoes:
        escritor.writerow(transacao)

print("Transações ordenadas com sucesso!")