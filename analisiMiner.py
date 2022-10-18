import pandas as pd
import os
import json


with open('L:\\TESI\\analisiCoinbase\\listaAddress.json') as fileJson:
    data_address_miner = json.load(fileJson)

#print(data_address) #da qui lavoro su data_address

fileAddressCompleto = pd.read_csv("L:\\TESI\\analisiAddressLista\\lista_completa_address_con_balance.csv", sep=";", names=["address", "balance"])
fileAddressCompletop = pd.read_csv("L:\\TESI\\balances\\balances-0_214553.csv", sep=";", names=["address", "balance"])

#i = 0
#for i in range(0, 20, 1):
#    print("value balance ", fileAddressCompleto["balance"].values[i])
'''
print("**---------------------------------------------------**")
print("Gli indirizzi Bitcoin trovati sono: ", len(fileAddressCompleto))
print("I bitcoin posseduti in totale sono: ", fileAddressCompleto["balance"].sum()/100000000)
print("Bitcoin posseduti in media: ", (fileAddressCompleto["balance"].sum()/100000000)/len(fileAddressCompleto))
print("**---------------------------------------------------**")

print("Numero address con nan compresi: ", len(fileAddressCompleto))
valoriAddress_rimuovo_nan = fileAddressCompleto

#ora rimuovo gli address nan nulli
k = 0
for k in range(0, len(valoriAddress_rimuovo_nan) -1, 1):
    if valoriAddress_rimuovo_nan[k].get('address') == "nan":
        print("sono nell'if e ho trovato: ", valoriAddress_rimuovo_nan[k].get('address'))
        del valoriAddress_rimuovo_nan[k]

print("Rimuovo gli address nan e rimangono ", len(valoriAddress_rimuovo_nan), "address")

'''
j = 0
for address in data_address_miner:
    address_miner = str(address.get('address'))
    print("cerco address: ", address_miner)

    print("type address ", type(address_miner))
    print("type address ", type(address.get('address')))

    print("type balance ", type(address_miner))
    print("type balance ", type(address.get('balance')))

    for j in range(0, len(fileAddressCompleto), 1):

        if address_miner == str(fileAddressCompleto["address"].values[j]):
            address['balance'] = int(fileAddressCompleto["address"].values[j])
            print("--------MINER---------")
            print("questo è l'address: ", address_miner)
            print("questo è l'address: ", str(fileAddressCompleto["address"].values[j]))
            print("questo è il balance: ", address['balance'])
            print("questo è il balance: ", int(fileAddressCompleto["address"].values[j]))

    fileJson = open('L:\\TESI\\analisiAddressLista\\lista_completa_address_miner_con_balance.json', 'w')
    fileJson.writelines(json.dumps(data_address_miner))
    fileJson.close()

#listaAddressMiner


'''
for address in data_address:

    address_cerco_balance = address.get('address')

    for i in range(0, len(fileAddressCompleto), 1):

        if address_cerco_balance == str(fileAddressCompleto["address"].values[i]):
            address['balance'] = int(fileAddressCompleto["address"].values[i])
            print("questo è il data_address: ", data_address)

        for d in data_address:

            print("sto cercando ", d["address"])
            print("sto cercando ", d["balance"])
            if d.get("balance") != 0:
                print("ECCOLO---------------------------------------------------------")
                print(d['balance'])


'''



