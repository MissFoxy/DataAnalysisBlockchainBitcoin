import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

valoriAddress = [0] #lista valori address bitcoin
tabella = []


fileCsvBalances0_214553 = pd.read_csv('T:\\file_csv_tesi\\balances-0_214553.csv', sep=";")

Total0_214553 = fileCsvBalances0_214553['balance'].sum()
TotalEffettivo0_214553 = Total0_214553 / 100000000
inMedia0_214553 = TotalEffettivo0_214553 / len(fileCsvBalances0_214553)
print("Media bitcoin posseduti dal singolo utente, dalla nascita al 31 Dicembre 2012:")
print(inMedia0_214553)
valoriAddress.append(inMedia0_214553)
tabella.append(('2009-2012', '|', 'blocchi 0 - 214553', '|', inMedia0_214553))

####---------------------------------####

fileCsvBalances214554_446026 = pd.read_csv('T:\\file_csv_tesi\\balances-214554_446026.csv', sep=";")
# (dal blocco 214554 al blocco 446026)
Total214554_446026 = fileCsvBalances214554_446026['balance'].sum()
TotalEffettivo214554_446026 = Total214554_446026 / 100000000
inMedia214554_446026 = TotalEffettivo214554_446026 / len(fileCsvBalances214554_446026)
print("Media bitcoin posseduti dal singolo utente, dal 1 Gennaio 2013 al 31 Dicembre 2016:")
print(inMedia214554_446026)
valoriAddress.append(inMedia214554_446026)
tabella.append(('2013-2016', '|', 'blocchi 214554 - 446026', '|', inMedia214554_446026))

####---------------------------------####

fileCsvBalances446027_501950 = pd.read_csv('T:\\file_csv_tesi\\balances-446027_501950.csv', sep=";")

Total446027_501950 = fileCsvBalances446027_501950['balance'].sum()
TotalEffettivo446027_501950 = Total446027_501950 / 100000000
inMedia446027_501950 = TotalEffettivo446027_501950 / len(fileCsvBalances446027_501950)
print("Media bitcoin posseduti dal singolo utente, nell'anno 2017:")
print(inMedia446027_501950)
valoriAddress.append(inMedia446027_501950)
tabella.append(('2017', '|', 'blocchi 446027 - 501950', '|', inMedia446027_501950))

####---------------------------------####

fileCsvBalances501951_610680 = pd.read_csv('T:\\file_csv_tesi\\balances-501951_610680.csv', sep=";")

Total501951_610680 = fileCsvBalances501951_610680['balance'].sum()
TotalEffettivo501951_610680 = Total501951_610680 / 100000000
inMedia501951_610680 = TotalEffettivo501951_610680 / len(fileCsvBalances501951_610680)
print("Media bitcoin posseduti dal singolo utente, dal 1 Gennaio 2018 fino a dicembre 2019:")
print(inMedia501951_610680)
valoriAddress.append(inMedia501951_610680)
tabella.append(('2018-2019', '|', 'blocchi 501951 - 610680', '|', inMedia501951_610680))

#print(valoriAddress)

#--TABELLA--#

x = ['2009', '2009-2012', '2013-2016', '2017', '2018-2019']

plt.plot(x, valoriAddress, marker=".", markersize=10, color='orange')

plt.xlabel('Anno')
plt.ylabel('bitcoin posseduti in media')
plt.title('Analisi del bilancio medio del singolo utente')
plt.grid(True)
plt.tight_layout() #migliora la visibilità
plt.show()

print('**---------------------------------------------------------------**')
labels = ['Periodo storico', '|', 'Intervallo blocchi', '|', 'Media Saldo']

dataframeTabella = pd.DataFrame(tabella, columns=labels)
print(dataframeTabella)
















