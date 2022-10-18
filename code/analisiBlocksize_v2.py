import pandas as pd
import os
import glob
import matplotlib.pyplot as plt

valoriBlocksize = [] #lista valori Blocksize


###----------------------------------###
pathBlocks0_214553 = "T:\\file_csv_tesi\\blocks\\2009-2012\\"
csv_filesBlocks0_214553 = glob.glob(os.path.join(pathBlocks0_214553, "*.csv"))

pathBlocks214554_446026 = "T:\\file_csv_tesi\\blocks\\2013-2016\\"
csv_filesBlocks214554_446026 = glob.glob(os.path.join(pathBlocks214554_446026, "*.csv"))

pathBlocks446027_501950 = "T:\\file_csv_tesi\\blocks\\2017\\"
csv_filesBlocks446027_501950 = glob.glob(os.path.join(pathBlocks446027_501950, "*.csv"))

pathBlocks501951_610680 = "T:\\file_csv_tesi\\blocks\\2018-2019\\"
csv_filesBlocks501951_610680 = glob.glob(os.path.join(pathBlocks501951_610680, "*.csv"))

for fileBlocks in csv_filesBlocks0_214553:
    fileCsvBlocks = pd.read_csv(fileBlocks, sep = ";")

    totalSize = fileCsvBlocks['blocksize'].sum()
    totalEffettivoSize = totalSize / 1000
    inMediaSize = totalEffettivoSize / len(fileCsvBlocks)
    valoriBlocksize.append(inMediaSize)

valoriBlocksize214554_446026 = []
for fileBlocks in csv_filesBlocks214554_446026:
    fileCsvBlocks = pd.read_csv(fileBlocks, sep = ";")

    totalSize = fileCsvBlocks['blocksize'].sum()
    totalEffettivoSize = totalSize / 1000
    inMediaSize = totalEffettivoSize / len(fileCsvBlocks)
    valoriBlocksize214554_446026.append(inMediaSize)

inMedia2013_2016 = (sum(valoriBlocksize214554_446026))/4
valoriBlocksize.append(inMedia2013_2016)

valoriBlocksize446027_501950 = []
for fileBlocks in csv_filesBlocks446027_501950:
    fileCsvBlocks = pd.read_csv(fileBlocks, sep = ";")

    totalSize = fileCsvBlocks['blocksize'].sum()
    totalEffettivoSize = totalSize / 1000
    inMediaSize = totalEffettivoSize / len(fileCsvBlocks)
    valoriBlocksize446027_501950.append(inMediaSize)

inMedia2017 = (sum(valoriBlocksize446027_501950)) /2
valoriBlocksize.append(inMedia2017)

valoriBlocksize501951_610680 = []
for fileBlocks in csv_filesBlocks501951_610680:
    fileCsvBlocks = pd.read_csv(fileBlocks, sep = ";")

    totalSize = fileCsvBlocks['blocksize'].sum()
    totalEffettivoSize = totalSize / 1000
    inMediaSize = totalEffettivoSize / len(fileCsvBlocks)
    valoriBlocksize501951_610680.append(inMediaSize)

inMedia2018_2019 = (sum(valoriBlocksize501951_610680)) /2
valoriBlocksize.append(inMedia2018_2019)


#--TABELLA--#
x = ['2009-2012', '2013-2016', '2017', '2018-2019']


plt.plot(x, valoriBlocksize, marker=".", markersize=10, color='red')
plt.xlabel('Anno')
plt.ylabel('Blocksize (in bytes) media')
plt.title('Analisi blocksize')
plt.grid(True)
plt.tight_layout()
plt.show()

sbarre = ["|", "|", "|", "|"]
tabellaRiassuntiva = pd.DataFrame(data = {"Periodo storico": x, "|":sbarre, "Blocksize (in bytes) media" : valoriBlocksize})
print(tabellaRiassuntiva)