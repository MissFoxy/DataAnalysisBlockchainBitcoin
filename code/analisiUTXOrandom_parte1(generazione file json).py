import pandas as pd
import os
import subprocess
import json
import glob
import random

data_utxo = [ {"output" : "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b", "generato" : 0, "speso" : " null"}] #per prova metto la primissima
print(data_utxo)

for i in range(1, 698461, 10000):
    i2 = i + 1
    i = str(i)
    i2 = repr(i2)
    rustycommand = "rusty-blockparser -d T:/BitcoinCore_dati/blocks -s " + i + " -e " + i2 + " unspentcsvdump L:/TESI/analisiUTXO"
    subprocess.check_output(['git-bash.exe', '-c', rustycommand])
    print(rustycommand)

    fileCsvUnspent = pd.read_csv('L:\\TESI\\analisiUTXO\\unspent-0-1.csv', sep=";") #, names = ["txid", "indexOut", "height", "value", "address"])

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

df = pd.DataFrame.from_dict(data_utxo)
df.to_csv(os.path.join("L:\\TESI\\analisiUTXO\\", "dump_UTXO_randomPROVA70.csv"))
print(df)

fileJson = open('L:\\TESI\\analisiUTXO\\dump_in_jsonPROVA70.json', 'w')
fileJson.writelines(json.dumps(data_utxo))
fileJson.close()

fileJson = open('L:\\TESI\\analisiUTXO\\dump_in_jsonPROVA70.json', "r")
print("Output del file json")
print(fileJson.read())
fileJson.close()

print("questa è la lunghezza di data_utxo: ", len(data_utxo))