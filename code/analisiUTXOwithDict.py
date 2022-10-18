import pandas as pd
import os
import subprocess
import json
import glob

os.chdir("C:\\Program Files\\Git")
pathUnspent = "T:\\file_csv_tesi\\script_UXTO"
csv_filesUnspent = glob.glob(os.path.join(pathUnspent, "*.csv"))

data_utxo = [ {"output" : "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b", "generato" : 0, "speso" : " null"}] #per prova metto la primissima
print(json.dumps(data_utxo))

for i in range(600000, 605000, 1):
    i2 = i + 1
    i = str(i)
    i2 = repr(i2)
    rustycommand = "rusty-blockparser -d T:/BitcoinCore_dati/blocks -s " + i + " -e " + i2 + " unspentcsvdump T:/file_csv_tesi/script_UXTO"
    subprocess.check_output(['git-bash.exe', '-c', rustycommand])


    print(rustycommand)

    ###prendo il file, tanto è uno ed ha sempre lo stesso nome
    fileCsvUnspent = pd.read_csv('T:\\file_csv_tesi\\script_UXTO\\unspent-0-1.csv', sep=";")

    for num in range(0, len(fileCsvUnspent), 1):
        txid = str(fileCsvUnspent['txid'].values[num])

        #print(data_utxo)
        #print((len(data_utxo)))

        for p in data_utxo:
            if p.get('output') == txid: # and p.get("generato") != i):
                p['speso'] = i
            else:
                data_utxo.append({"output": txid, "generato": i, "speso": "null"})
                break

    #next((item for item in data_utxo if item["output"] == txid), print("wat")) studia come si usa questo comando
    #print(json.dumps(data_utxo))


print(json.dumps(data_utxo)) #, indent = 4))

df = pd.DataFrame.from_dict(data_utxo) #, orient='index', columns=['P', 'Q', 'R'])

print(df)

#df.to_csv(os.path.join("C:\\Users\\scrib\\Desktop\\csv dump", "csv_dump_UTXO_tabella.csv"))
df.to_csv(os.path.join("L:\\", "csv_dump_UTXO_tabella.csv"))


