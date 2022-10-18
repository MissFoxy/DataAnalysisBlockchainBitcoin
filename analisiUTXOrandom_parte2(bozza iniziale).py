import pandas as pd
import os
import json
import glob

pathUnspent = "L:\\TESI\\unspent\\"
csv_filesUnspent = glob.glob(os.path.join(pathUnspent, "*.csv"))

with open('L:\\TESI\\analisiUTXO\\dump_in_jsonPROVA70(file_esempio).json') as fileJson:
    data_utxo = json.load(fileJson)

print(data_utxo) #da qui lavoro su data_utxo


for t in data_utxo:
    utxo_da_cercare = t.get('output')

    print("sta cercando: ", utxo_da_cercare)

    for fileUnspent_globali in csv_filesUnspent:
        fileUnspent = pd.read_csv(fileUnspent_globali, sep=";")

        print('File location:', fileUnspent_globali)
        print('File Name:', fileUnspent_globali.split("\\")[-1])


        for j in range(0, len(fileUnspent), 1):


            if fileUnspent["txid"].values[j] == utxo_da_cercare and t['generato'] != fileUnspent["height"].values[j]:
                print("j: ", j)
                print("t['generato']", t['generato'])
                print("t['generato']", t.get('generato'))
                print("fileUnspent[height].values[j]", fileUnspent["height"].values[j])

                t['speso'] = fileUnspent["height"].values[j]
                print("sono nell'if <3")
                break

            '''
            print("prima del secondo if t[speso]", t['speso'])
            print("type ", type(t['speso']))
            print("type null", type(stringa_null))

            campo_dict = t.get('speso')
            stringa_null = "null"
            if campo_dict != stringa_null:
                print("Sono nel secondo if", j)
                break
            '''


df = pd.DataFrame.from_dict(data_utxo)
df.to_csv(os.path.join("L:\\TESI\\analisiUTXO\\", "dump_UTXO_randomCompletato.csv"))
print(df)