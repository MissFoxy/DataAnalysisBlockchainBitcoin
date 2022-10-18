import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

valoriAddress = [0] #lista valori address bitcoin

pathBalances = "T:\\file_csv_tesi\\balances\\"
csv_filesBalances = glob.glob(os.path.join(pathBalances, "*.csv"))

for fileBalances in csv_filesBalances:
    fileCsvBalances = pd.read_csv(fileBalances, sep = ";")
    total = fileCsvBalances['balance'].sum()
    totalEffettivo = total / 100000000
    inMedia = totalEffettivo / len(fileCsvBalances)
    valoriAddress.append(inMedia)


###############################################################################################

valueUnspentMedia = [0]

pathUnspent = "T:\\file_csv_tesi\\unspent\\"
csv_filesUnspent = glob.glob(os.path.join(pathUnspent, "*.csv"))

for filesUnspent in csv_filesUnspent:
    fileCsvUnspent = pd.read_csv(filesUnspent, sep=";")
    heightMedia = fileCsvUnspent['height'].sum() / len(fileCsvUnspent)
    valueMedia = (fileCsvUnspent['value'].sum() / 1000000000) / len(fileCsvUnspent)
    valueUnspentMedia.append(valueMedia)
    print("Valore medio delle UXTO ")
    print(valueMedia)



#--TABELLA--#

#x = [2009, 2012, 2016, 2017, 2019]
x = ['2009', '2009-2012', '2013-2016', '2017', '2018-2019', '2020-2021']

plt.plot(x, valoriAddress, marker=".", markersize=10, color='orange', label='Balance medio')
plt.plot(x, valueUnspentMedia, marker=".", markersize = 10, color='blue', label='Valore medio UTXO')

plt.xlabel('Anno')
plt.ylabel('bitcoin in media')
plt.title('Analisi media bitcoin')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

print("*-------------------------------------------------------*")
tabellaRiassuntiva = pd.DataFrame(data = {"Periodo": x, "Valore medio balance": valoriAddress, "Valore medio UTXO": valueUnspentMedia})
print(tabellaRiassuntiva)