import csv

saldos = {}

with open("transacoes_ordenadas.csv", "r", newline="", encoding="utf-8") as arquivo:

    leitor = csv.DictReader(arquivo)

    for transacao in leitor:

        data = transacao["Data"]
        tipo = transacao["Tipo"]
        valor = float(transacao["Valor"])

        if data not in saldos:
            saldos[data] = {
                "operacoes": 0,
                "creditos": 0,
                "debitos": 0
            }

        saldos[data]["operacoes"] += 1

        if tipo == "C":
            saldos[data]["creditos"] += valor

        elif tipo == "D":
            saldos[data]["debitos"] += valor


print("===== SALDO DIÁRIO =====")

for data, dados in saldos.items():

    saldo = dados["creditos"] - dados["debitos"]

    print(f"\nData: {data}")
    print(f"Operações: {dados['operacoes']}")
    print(f"Créditos: R$ {dados['creditos']:.2f}")
    print(f"Débitos: R$ {dados['debitos']:.2f}")
    print(f"Saldo: R$ {saldo:.2f}")