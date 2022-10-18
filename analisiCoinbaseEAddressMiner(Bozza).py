import pandas as pd
import os
import subprocess
import json
import glob

import random


#analisi prova sul blocco 500000

pathUnspent = "L:\\TESI\\analisiCoinbase"
csv_filesUnspent = glob.glob(os.path.join(pathUnspent, "*.csv"))

'''
for filesUnspent in csv_filesUnspent:
    fileCsvUnspent = pd.read_csv(filesUnspent, sep=";")
    heightUnspentMediaV = fileCsvUnspent['height'].sum() / len(fileCsvUnspent)
    valueUnspentMediaV = (fileCsvUnspent['value'].sum() / 1000000000) / len(fileCsvUnspent)
    heightUnspentMedia.append(heightUnspentMediaV)
    valueUnspentMedia.append(valueUnspentMediaV)
'''

'''
fileIn = pd.read_csv("L:\\TESI\\analisiCoinbase\\tx_in-0-1.csv", sep=";", names = ["txid", "hashPrevOut", "indexPrevOut", "scriptSig", "sequence"])
fileOut = pd.read_csv("L:\\TESI\\analisiCoinbase\\tx_out-0-1.csv", sep=";", names=["txid", "indexOut", "height", "value", "scriptPubKey", "address"])
fileTransactions = pd.read_csv("L:\\TESI\\analisiCoinbase\\transactions-0-1.csv", sep=";", names=["txid", "hashBlock", "version", "lockTime"])

#1 metodo, prendo ogni id in trans e lo cerco in file out

counterTrovato = 0
i = 0
j = 0
for i in range(len(fileTransactions)):
    id = fileTransactions["txid"].values[i]
    print(type(id))
    print("ecco l'id:", id)
    for j in range(len(fileOut)):
        print(type(fileOut["txid"].values[j]))
        print("ecco fileOut[txid].values[j]:", id)
        if (id == fileOut["txid"].values[j]):
            print("trovato")
            counterTrovato = counterTrovato + 1
        else:
            print("questo id non è nel file out")
            break
'''

listaAddress = []
x = random.randint(0,50)

print(x)



os.chdir("C:\\Program Files\\Git")
#pathUnspent = "L:\\TESI\\analisiCoinbase\\"
#csv_filesUnspent = glob.glob(os.path.join(pathUnspent, "*.csv"))

#prove
for i in range(1, 2000, 1):
    i2 = i + 1
    i = str(i)
    i2 = repr(i2)
    rustycommand = "rusty-blockparser -d T:/BitcoinCore_dati/blocks -s " + i + " -e " + i2 + " csvdump L:/TESI/analisiCoinbase/"
    subprocess.check_output(['git-bash.exe', '-c', rustycommand])

    fileOut = pd.read_csv("L:\\TESI\\analisiCoinbase\\tx_out-0-1.csv", sep=";", names=["txid", "indexOut", "value", "scriptPubKey", "address"])

    print(fileOut["address"].values[0])

    listaAddress.append(fileOut["address"].values[0])

    print(listaAddress)









