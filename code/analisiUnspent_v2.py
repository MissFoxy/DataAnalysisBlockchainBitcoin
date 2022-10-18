import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

heightUnspentMedia = []
valueUnspentMedia = []

pathUnspent = "T:\\file_csv_tesi\\unspent\\"
csv_filesUnspent = glob.glob(os.path.join(pathUnspent, "*.csv"))

for filesUnspent in csv_filesUnspent:
    fileCsvUnspent = pd.read_csv(filesUnspent, sep=";")
    heightUnspentMediaV = fileCsvUnspent['height'].sum() / len(fileCsvUnspent)
    valueUnspentMediaV = (fileCsvUnspent['value'].sum() / 1000000000) / len(fileCsvUnspent)
    heightUnspentMedia.append(heightUnspentMediaV)
    valueUnspentMedia.append(valueUnspentMediaV)
    '''
    print("Valore medio delle UXTO ")
    print(valueUnspentMediaV)
    print('La rispettiva altezza dei blocchi è in media ')
    print(heightUnspentMediaV)
    '''


####------------------------------####

plt.plot(heightUnspentMedia, valueUnspentMedia, marker=".", markersize = 10, color='orange')

#plt.bar(heightUnspentMedia, valueUnspentMedia, width = 0.8, color = ['red', 'green']) poi magari lavoraci

plt.xlabel('Altezza blocchi')
plt.ylabel('Valore in media')
plt.title('Analisi UTXO')
plt.grid(True)
plt.tight_layout()
plt.show()

print('**---------------------------------------------------------------**')
#labels = ['Periodo storico', '|', 'Intervallo blocchi', '|', 'Altezza blockchain', '|', 'Media valore UTXO']
periodoStorico = ['2009-2012', '2013-2016', '2017', '2018-2019']
#intervalloBlocchi = ['blocchi 0 - 214553', 'blocchi 214554 - 446026', 'blocchi 446027 - 501950', 'blocchi 501951 - 610680', ]

sbarre = ["|", "|", "|", "|"]
#sbarre2 = ["|", "|", "|", "|"]
#tabellaRiassuntiva = pd.DataFrame(data = {"Periodo storico": periodoStorico , "|": sbarre, "Intervallo blocchi" : intervalloBlocchi, "Altezza blockchain" : heightUnspentMedia, "Media valore UTXO" : valueUnspentMedia})
tabellaRiassuntiva = pd.DataFrame(data = {"Periodo storico": periodoStorico , "|": sbarre, "Altezza blockchain" : heightUnspentMedia,  "Media valore UTXO" : valueUnspentMedia})
print(tabellaRiassuntiva)