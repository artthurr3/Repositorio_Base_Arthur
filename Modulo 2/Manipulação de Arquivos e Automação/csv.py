import csv

arquivo = open("dados.csv")
leia = csv.DictReader(arquivo)
for linha in leia:

    print(linha)
if linha["marca"] == "ford":
    print(linha)
