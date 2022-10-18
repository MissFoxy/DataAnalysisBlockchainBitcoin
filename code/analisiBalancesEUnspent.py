import pandas as pd
import matplotlib.pyplot as plt

valoriAddress = [0] #lista valori address bitcoin

fileCsvBalances0_214553 = pd.read_csv('T:\\file_csv_tesi\\balances-0_214553.csv', sep=";")

Total0_214553 = fileCsvBalances0_214553['balance'].sum()
TotalEffettivo0_214553 = Total0_214553 / 100000000
inMedia0_214553 = TotalEffettivo0_214553 / len(fileCsvBalances0_214553)
print("Media bitcoin posseduti dal singolo utente, dalla nascita al 31 Dicembre 2012:")
print(inMedia0_214553)
valoriAddress.append(inMedia0_214553)

####---------------------------------####

fileCsvBalances214554_446026 = pd.read_csv('T:\\file_csv_tesi\\balances-214554_446026.csv', sep=";")
# (dal blocco 214554 al blocco 446026)
Total214554_446026 = fileCsvBalances214554_446026['balance'].sum()
TotalEffettivo214554_446026 = Total214554_446026 / 100000000
inMedia214554_446026 = TotalEffettivo214554_446026 / len(fileCsvBalances214554_446026)
print("Media bitcoin posseduti dal singolo utente, dal 1 Gennaio 2013 al 31 Dicembre 2016:")
print(inMedia214554_446026)
valoriAddress.append(inMedia214554_446026)

####---------------------------------####

fileCsvBalances446027_501950 = pd.read_csv('T:\\file_csv_tesi\\balances-446027_501950.csv', sep=";")

Total446027_501950 = fileCsvBalances446027_501950['balance'].sum()
TotalEffettivo446027_501950 = Total446027_501950 / 100000000
inMedia446027_501950 = TotalEffettivo446027_501950 / len(fileCsvBalances446027_501950)
print("Media bitcoin posseduti dal singolo utente, nell'anno 2017:")
print(inMedia446027_501950)
valoriAddress.append(inMedia446027_501950)

####---------------------------------####

fileCsvBalances501951_610680 = pd.read_csv('T:\\file_csv_tesi\\balances-501951_610680.csv', sep=";")

Total501951_610680 = fileCsvBalances501951_610680['balance'].sum()
TotalEffettivo501951_610680 = Total501951_610680 / 100000000
inMedia501951_610680 = TotalEffettivo501951_610680 / len(fileCsvBalances501951_610680)
print("Media bitcoin posseduti dal singolo utente, dal 1 Gennaio 2018 fino a dicembre 2019:")
print(inMedia501951_610680)
valoriAddress.append(inMedia501951_610680)

#print(valoriAddress)



###############################################################################################

valueUnspentMedia = [0]

fileCsvUnspent0_214553 = pd.read_csv('T:\\file_csv_tesi\\unspent-0_214553.csv', sep=";")

heightMedia_0_214553 = fileCsvUnspent0_214553['height'].sum() / len(fileCsvUnspent0_214553)
valueMedia_0_214553 = (fileCsvUnspent0_214553['value'].sum() /1000000000 ) / len(fileCsvUnspent0_214553)
valueUnspentMedia.append(valueMedia_0_214553)
print('Valore medio delle UXTO nel periodo dalla nascita al 31 Dicembre 2012: ')
print(valueMedia_0_214553)


####------------------------------####

fileCsvUnspent214554_446026 = pd.read_csv('T:\\file_csv_tesi\\unspent-214554_446026.csv', sep=";")

heightMedia_214554_446026 = fileCsvUnspent214554_446026['height'].sum() / len(fileCsvUnspent214554_446026)
valueMedia_214554_446026 = (fileCsvUnspent214554_446026['value'].sum() /1000000000 ) / len(fileCsvUnspent214554_446026)
valueUnspentMedia.append(valueMedia_214554_446026)
print('Valore medio delle UXTO nel periodo dal 1 Gennaio 2013 al 31 Dicembre 2016: ')
print(valueMedia_214554_446026)


####------------------------------####

fileCsvUnspent446027_501950 = pd.read_csv('T:\\file_csv_tesi\\unspent-446027_501950.csv', sep=";")

heightMedia_446027_501950 = fileCsvUnspent446027_501950['height'].sum() / len(fileCsvUnspent446027_501950)
valueMedia_446027_501950 = (fileCsvUnspent446027_501950['value'].sum() /1000000000 ) / len(fileCsvUnspent446027_501950)
valueUnspentMedia.append(valueMedia_446027_501950)
print("Valore medio delle UXTO nel periodo nell'anno 2017: ")
print(valueMedia_446027_501950)

####------------------------------####

fileCsvUnspent501951_610680 = pd.read_csv('T:\\file_csv_tesi\\unspent-501951_610680.csv', sep=";")

heightMedia_501951_610680 = fileCsvUnspent501951_610680['height'].sum() / len(fileCsvUnspent501951_610680)
valueMedia_501951_610680 = (fileCsvUnspent501951_610680['value'].sum() /1000000000 ) / len(fileCsvUnspent501951_610680)
valueUnspentMedia.append(valueMedia_501951_610680)
print("Valore medio delle UXTO nel periodo dal 1 Gennaio 2018 fino a dicembre 2019: ")
print(valueMedia_501951_610680)

####------------------------------####

print(valueUnspentMedia)

#--TABELLA--#

#x = [2009, 2012, 2016, 2017, 2019]
x = ['2009', '2009-2012', '2013-2016', '2017', '2018-2019']

plt.plot(x, valoriAddress, marker=".", markersize=10, color='orange', label='Saldo medio')
plt.plot(x, valueUnspentMedia, marker=".", markersize = 10, color='blue', label='Valore medio UTXO')

plt.xlabel('Anno')
plt.ylabel('bitcoin in media')
plt.title('Analisi media bitcoin')
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
