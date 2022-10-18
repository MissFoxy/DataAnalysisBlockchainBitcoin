import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

valoriAddress = [] #lista valori address bitcoin
#tabella = pd.DataFrame({"Periodo": [0], "Media": [0]})


pathBalances = "T:\\file_csv_tesi\\balances\\"
csv_files = glob.glob(os.path.join(pathBalances, "*.csv"))

for fileBalances in csv_files:
    fileCsvBalances = pd.read_csv(fileBalances, sep = ";")
    total = fileCsvBalances['balance'].sum()
    totalEffettivo = total / 100000000
    inMedia = totalEffettivo / len(fileCsvBalances)
    valoriAddress.append(inMedia)


#--TABELLA--#
x = [ '2009-2012', '2013-2016', '2017', '2018-2019', '2020-2021']

plt.plot(x, valoriAddress, marker=".", markersize=10, color='orange')

plt.xlabel('Anno')
plt.ylabel('bitcoin posseduti in media')
plt.title('Analisi del bilancio medio del singolo utente')
plt.grid(True)
plt.tight_layout() #migliora la visibilità
plt.show()

print('**----------------------**')


tabella = pd.DataFrame(data = {"Periodo": x, "Media": valoriAddress})
print(tabella)