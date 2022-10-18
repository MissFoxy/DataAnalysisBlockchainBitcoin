import pandas as pd
import matplotlib.pyplot as plt

heightUnspentMedia = []
valueUnspentMedia = []
tabellaUnspent = []

fileCsvUnspent0_214553 = pd.read_csv('T:\\file_csv_tesi\\unspent-0_214553.csv', sep=";")

heightMedia_0_214553 = fileCsvUnspent0_214553['height'].sum() / len(fileCsvUnspent0_214553)
valueMedia_0_214553 = (fileCsvUnspent0_214553['value'].sum() /1000000000 ) / len(fileCsvUnspent0_214553)
heightUnspentMedia.append(heightMedia_0_214553)
valueUnspentMedia.append(valueMedia_0_214553)
print('Valore medio delle UXTO nel periodo dalla nascita al 31 Dicembre 2012: ')
print(valueMedia_0_214553)
print('La rispettiva altezza dei blocchi è in media ')
print(heightMedia_0_214553)
tabellaUnspent.append(('2009-2012', '|', 'blocchi 0 - 214553', '|', heightMedia_0_214553, '|', valueMedia_0_214553))

####------------------------------####

fileCsvUnspent214554_446026 = pd.read_csv('T:\\file_csv_tesi\\unspent-214554_446026.csv', sep=";")

heightMedia_214554_446026 = fileCsvUnspent214554_446026['height'].sum() / len(fileCsvUnspent214554_446026)
valueMedia_214554_446026 = (fileCsvUnspent214554_446026['value'].sum() /1000000000 ) / len(fileCsvUnspent214554_446026)
heightUnspentMedia.append(heightMedia_214554_446026)
valueUnspentMedia.append(valueMedia_214554_446026)
print('Valore medio delle UXTO nel periodo dal 1 Gennaio 2013 al 31 Dicembre 2016: ')
print(valueMedia_214554_446026)
print('La rispettiva altezza dei blocchi è in media ')
print(heightMedia_214554_446026)
tabellaUnspent.append(('2013-2016', '|', 'blocchi 214554 - 446026', '|', heightMedia_214554_446026, '|', valueMedia_214554_446026))

####------------------------------####

fileCsvUnspent446027_501950 = pd.read_csv('T:\\file_csv_tesi\\unspent-446027_501950.csv', sep=";")

heightMedia_446027_501950 = fileCsvUnspent446027_501950['height'].sum() / len(fileCsvUnspent446027_501950)
valueMedia_446027_501950 = (fileCsvUnspent446027_501950['value'].sum() /1000000000 ) / len(fileCsvUnspent446027_501950)
heightUnspentMedia.append(heightMedia_446027_501950)
valueUnspentMedia.append(valueMedia_446027_501950)
print("Valore medio delle UXTO nel periodo nell'anno 2017: ")
print(valueMedia_446027_501950)
print("La rispettiva altezza dei blocchi è in media ")
print(heightMedia_446027_501950)
tabellaUnspent.append(('2017', '|', 'blocchi 446027 - 501950', '|', heightMedia_446027_501950, '|', valueMedia_446027_501950))

####------------------------------####

fileCsvUnspent501951_610680 = pd.read_csv('T:\\file_csv_tesi\\unspent-501951_610680.csv', sep=";")

heightMedia_501951_610680 = fileCsvUnspent501951_610680['height'].sum() / len(fileCsvUnspent501951_610680)
valueMedia_501951_610680 = (fileCsvUnspent501951_610680['value'].sum() /1000000000 ) / len(fileCsvUnspent501951_610680)
heightUnspentMedia.append(heightMedia_501951_610680)
valueUnspentMedia.append(valueMedia_501951_610680)
print("Valore medio delle UXTO nel periodo dal 1 Gennaio 2018 fino a dicembre 2019: ")
print(valueMedia_501951_610680)
print("La rispettiva altezza dei blocchi è in media ")
print(heightMedia_501951_610680)
tabellaUnspent.append(('2018-2019', '|', 'blocchi 501951 - 610680', '|', heightMedia_501951_610680, '|', valueMedia_501951_610680))

####------------------------------####

plt.plot(heightUnspentMedia, valueUnspentMedia, marker=".", markersize = 10, color='orange')

#plt.bar(heightUnspentMedia, valueUnspentMedia, width = 0.8, color = ['red', 'green'])

plt.xlabel('Altezza blocchi')
plt.ylabel('Valore in media')
plt.title('Analisi UTXO')
plt.grid(True)
plt.tight_layout()
plt.show()

print('**---------------------------------------------------------------------------------------------------**')
labels = ['Periodo storico', '|', 'Intervallo blocchi', '|', 'Altezza blockchain', '|', 'Media valore UTXO']

dataframeTabellaUnspent = pd.DataFrame(tabellaUnspent, columns=labels)
print(dataframeTabellaUnspent)