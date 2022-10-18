import pandas as pd
import os
import json
import glob
import matplotlib.pyplot as plt

#analisi dei balances attuali, totali

valoriAddress = [{"address" : "null", "balance" : 1}]


print(type(valoriAddress))

pathBalances = "L:\\TESI\\balances"
csv_files = glob.glob(os.path.join(pathBalances, "*.csv"))

for fileBalances in csv_files:
    fileCsvBalances = pd.read_csv(fileBalances, sep = ";")

    print('File location:', fileBalances)
    print('File Name:', fileBalances.split("\\")[-1])

    print(type(valoriAddress))

    df = pd.DataFrame.from_dict(valoriAddress)
    print(df)

    for num in range(0, len(fileCsvBalances), 1):

        address = str(fileCsvBalances["address"].values[num])
        balances = int(fileCsvBalances["balance"].values[num])

        for p in valoriAddress:

            if p.get('address') == address:
                p['balance'] = p['balance'] + balances
            else:
                valoriAddress.append({"address": address, "balance": balances})
                print(valoriAddress)
                break


#print(json.dumps(valoriAddress)) #per printarli decentemente

print(type(valoriAddress))

df = pd.DataFrame.from_dict(valoriAddress)

df.to_csv(os.path.join("L:\\TESI\\analisiAddressLista\\", "lista_completa_address_con_balancePROVA.csv"))

print(df)

print("ORA INIZIA L'ANALISI SUL FILE")


fileCsvBalancesTotal = pd.read_csv('L:\\TESI\\analisiAddressLista\\lista_completa_address_con_balancePROVA.csv', sep=",", names = ["address", "balance"], low_memory=False)

Total = 0
j = 0
for j in range(0, len(fileCsvBalancesTotal), 1):
    Total = Total + int(fileCsvBalancesTotal['balance'].sum())

#Total = fileCsvBalancesTotal['balance'].sum()
print("total: ", Total)
TotalEffettivo = Total / 100000000
print("total effettivo: ", TotalEffettivo)
inMedia = TotalEffettivo / len(fileCsvBalancesTotal)
print("in media: ", inMedia)

print("**-----------------------------------------------------------------------------**")
#print("NB: Analisi fatta su tutti gli indirizzi Bitcoin esistenti, non divisa per periodi")
print(("Il numero tolale di indirizzi bitcoin esistenti attualmente è:" ),  len(fileCsvBalancesTotal)) #con balance diverso da 0
print("In media il numero di bitcoin posseduti è: ", inMedia)
print("Il numero di bitcoin totali esistenti fino al 31 Agosto 2021 è: ", Total)
print("**-----------------------------------------------------------------------------**")


