import pandas as pd
import matplotlib.pyplot as plt

valoriBlocksize = [] #lista valori Blocksize
tabellaValoriBlocksize = []

###----------------------------------###
fileCsvBlocks0_214553 = pd.read_csv('T:\\file_csv_tesi\\blocks-0_214553.csv', sep=";")

totalSize0_214553 = fileCsvBlocks0_214553['blocksize'].sum()
totalEffettivoSize0_214553 = totalSize0_214553 / 1000
inMediaSize0_214553 = totalEffettivoSize0_214553 / len(fileCsvBlocks0_214553)
#print("Media blocksize in bytes dei blocchi, dalla nascita al 31 Dicembre 2012:")
#print(inMediaSize0_214553)
valoriBlocksize.append(inMediaSize0_214553)
tabellaValoriBlocksize.append(('2009-2012', '|', inMediaSize0_214553))


###----------------------------------###
fileCsvBlocks214554_272422 = pd.read_csv('T:\\file_csv_tesi\\blocks-214554_272422.csv', sep=";")
fileCsvBlocks272423_330290 = pd.read_csv('T:\\file_csv_tesi\\blocks-272423_330290.csv', sep=";")
fileCsvBlocks330291_388158 = pd.read_csv('T:\\file_csv_tesi\\blocks-330291_388158.csv', sep=";")
fileCsvBlocks388159_446026 = pd.read_csv('T:\\file_csv_tesi\\blocks-388159_446026.csv', sep=";")

totalSize214554_272422 = fileCsvBlocks214554_272422['blocksize'].sum()
totalEffettivoSize214554_272422 = totalSize214554_272422 / 1000
inMediaSize214554_272422 = totalEffettivoSize214554_272422 / len(fileCsvBlocks214554_272422)
#print("Media blocksize in bytes dei blocchi, dal 1 Gennaio 2013 al 31 Dicembre 2016:")
#print(inMediaSize214554_272422)
#valoriBlocksize.append(inMediaSize214554_272422)

totalSize272423_330290 = fileCsvBlocks272423_330290['blocksize'].sum()
totalEffettivoSize272423_330290 = totalSize272423_330290 / 1000
inMediaSize272423_330290 = totalEffettivoSize272423_330290 / len(fileCsvBlocks272423_330290)
#print("Media blocksize in bytes dei blocchi, dal 1 Gennaio 2013 al 31 Dicembre 2016:")
#print(inMediaSize272423_330290)
#valoriBlocksize.append(inMediaSize272423_330290)

totalSize330291_388158 = fileCsvBlocks330291_388158['blocksize'].sum()
totalEffettivoSize330291_388158 = totalSize330291_388158 / 1000
inMediaSize330291_388158 = totalEffettivoSize330291_388158 / len(fileCsvBlocks330291_388158)
#print("Media blocksize in bytes dei blocchi, dal 1 Gennaio 2013 al 31 Dicembre 2016:")
#print(inMediaSize330291_388158)
#valoriBlocksize.append(inMediaSize330291_388158)

totalSize388159_446026 = fileCsvBlocks388159_446026['blocksize'].sum()
totalEffettivoSize388159_446026 = totalSize388159_446026 / 1000
inMediaSize388159_446026 = totalEffettivoSize388159_446026 / len(fileCsvBlocks388159_446026)
#print("Media blocksize in bytes dei blocchi, dal 1 Gennaio 2013 al 31 Dicembre 2016:")
#print(inMediaSize388159_446026)
#valoriBlocksize.append(inMediaSize388159_446026)

inMedia2013_2016 = (inMediaSize214554_272422 + inMediaSize272423_330290 + inMediaSize330291_388158 + inMediaSize388159_446026)/4
tabellaValoriBlocksize.append(('2013-2016', '|', inMedia2013_2016))
valoriBlocksize.append(inMedia2013_2016)

###--------------2017--------------------###
fileCsvBlocks446027_473988 = pd.read_csv('T:\\file_csv_tesi\\blocks-446027_473988.csv', sep=";")

totalSize446027_473988 = fileCsvBlocks446027_473988['blocksize'].sum()
totalEffettivoSize446027_473988 = totalSize446027_473988 / 1000
inMediaSize446027_473988 = totalEffettivoSize446027_473988 / len(fileCsvBlocks446027_473988)
#print("Media blocksize in bytes dei blocchi, ")
#print(inMediaSize446027_473988)


fileCsvBlocks473989_501950 = pd.read_csv('T:\\file_csv_tesi\\blocks-473989_501950.csv', sep=";")

totalSize473989_501950 = fileCsvBlocks473989_501950['blocksize'].sum()
totalEffettivoSize473989_501950 = totalSize473989_501950 / 1000
inMediaSize473989_501950 = totalEffettivoSize473989_501950 / len(fileCsvBlocks473989_501950)
#print("Media blocksize in bytes dei blocchi, ")
#print(inMediaSize473989_501950)

inMedia2017 = (inMediaSize446027_473988 + inMediaSize473989_501950) /2
tabellaValoriBlocksize.append(('2017', '|', inMedia2017))
valoriBlocksize.append(inMedia2017)

###----------------------------------###
fileCsvBlocks501951_556315 = pd.read_csv('T:\\file_csv_tesi\\blocks-501951_556315.csv', sep=";")

totalSize501951_556315 = fileCsvBlocks501951_556315['blocksize'].sum()
totalEffettivoSize501951_556315 = totalSize501951_556315 / 1000
totalEffettivoSize501951_556315 = totalSize501951_556315 / 1000
inMediaSize501951_556315 = totalEffettivoSize501951_556315 / len(fileCsvBlocks501951_556315)
#print("Media blocksize in bytes dei blocchi, ")
#print(inMediaSize501951_556315)

fileCsvBlocks556316_610680 = pd.read_csv('T:\\file_csv_tesi\\blocks-556316_610680.csv', sep=";")

totalSize556316_610680 = fileCsvBlocks556316_610680['blocksize'].sum()
totalEffettivoSize556316_610680 = totalSize556316_610680 / 1000
inMediaSize556316_610680 = totalEffettivoSize556316_610680 / len(fileCsvBlocks556316_610680)
#print("Media blocksize in bytes dei blocchi, ")
#print(inMediaSize556316_610680)

inMedia2018_2019 = (inMediaSize501951_556315 + inMediaSize556316_610680) /2
tabellaValoriBlocksize.append(('2018-2019', '|', inMedia2018_2019))
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


print('**---------------------------------------------------**')
labels = ['Periodo storico', '|', 'Media blocksize (in bytes)']

dataframeTabellaValoriBlocksize = pd.DataFrame(tabellaValoriBlocksize, columns=labels)
print(dataframeTabellaValoriBlocksize)