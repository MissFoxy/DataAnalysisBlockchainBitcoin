import pandas as pd
import os
import subprocess
import json
import glob
import random
import csv

data_utxo = [ {"output" : "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b", "generato" : 0, "speso" : " null"}] #per prova metto la primissima
print(data_utxo)

'''
with open("L:\\TESI\\analisiUXTO\\dump_UXTO_random.csv", "r") as f:
    reader = csv.DictReader(f)
    lista = list(reader)
    print(lista)

data_utxo.append(lista)

print(json.dumps(data_utxo))
'''

for i in range(1, 700, 100):
    i2 = i + 1
    i = str(i)
    i2 = repr(i2)
    rustycommand = "rusty-blockparser -d T:/BitcoinCore_dati/blocks -s " + i + " -e " + i2 + " unspentcsvdump L:/TESI/analisiUXTO"
    subprocess.check_output(['git-bash.exe', '-c', rustycommand])
    print(rustycommand)

    ###prendo il file, tanto è uno ed ha sempre lo stesso nome
    fileCsvUnspent = pd.read_csv('L:\\TESI\\analisiUXTO\\unspent-0-1.csv', sep=";") #, names = ["txid", "indexOut", "height", "value", "address"])

    print("la lunghezza del file è:", len(fileCsvUnspent))
    x = random.randint(0, len(fileCsvUnspent) - 1)
    print("ecco il numero random: ", x)

    txid = fileCsvUnspent['txid'].values[x]
    print(txid)

    for p in data_utxo:
        if p.get('output') == txid:  # and p.get("generato") != i):
            p['speso'] = i
        else:
            data_utxo.append({"output": txid, "generato": i, "speso": "null"})
            break



#df = pd.read_json('strings.json',lines=True)
#print(df)

print("questo è il type di lista di dizionario: ", type(data_utxo))

print(json.dumps(data_utxo)) #per printarli decentemente

df = pd.DataFrame.from_dict(data_utxo)

df.to_csv(os.path.join("L:\\TESI\\analisiUXTO\\", "dump_UXTO_random.csv"))

print(df)

#1 prendo file json e lo converto in list of dicts
#2 uso il for e aggiorno la lista dicts
#3