import pandas as pd
from datetime import datetime

takeFistRow = pd.DataFrame({"hashblock": [0], "Valore_massimo": [0] })

fileCsvTransactions0_214553 = pd.read_csv('T:\\file_csv_tesi\\transactions-0_214553.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions0_214553 = pd.DataFrame(fileCsvTransactions0_214553.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions0_214553 = dataFrameTransactions0_214553.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)

dataFrameTransactions0_214553_MAX = pd.DataFrame({"hashblock": dataFrameTransactions0_214553['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions0_214553['Valore_massimo'].values[0]]})
print("vediamo il max:")
print(dataFrameTransactions0_214553_MAX)
print("-----------------------")

takeFistRow = takeFistRow.append(dataFrameTransactions0_214553_MAX)
print("vediamo:")
print(takeFistRow)
print("-----------------------")

##### ---------------------------------- #####

fileCsvTransactions214554_272422 = pd.read_csv('T:\\file_csv_tesi\\transactions-214554_272422.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions214554_272422 = pd.DataFrame(fileCsvTransactions214554_272422.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions214554_272422 = dataFrameTransactions214554_272422.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions214554_272422_MAX = pd.DataFrame({"hashblock": dataFrameTransactions214554_272422['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions214554_272422['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions214554_272422_MAX)
print(takeFistRow)
print("-----------------------")

##### ---------------------------------- #####


fileCsvTransactions272423_330290  = pd.read_csv('T:\\file_csv_tesi\\transactions-272423_330290.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions272423_330290 = pd.DataFrame(fileCsvTransactions272423_330290.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions272423_330290 = dataFrameTransactions272423_330290.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions272423_330290_MAX = pd.DataFrame({"hashblock": dataFrameTransactions272423_330290['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions272423_330290['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions272423_330290_MAX)
print(takeFistRow)
print("-----------------------")


##### ---------------------------------- #####

fileCsvTransactions330291_388158 = pd.read_csv('T:\\file_csv_tesi\\transactions-330291_388158.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions330291_388158 = pd.DataFrame(fileCsvTransactions330291_388158.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions330291_388158 = dataFrameTransactions330291_388158.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions330291_388158_MAX = pd.DataFrame({"hashblock": dataFrameTransactions330291_388158['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions330291_388158['Valore_massimo'].values[0]]})
bloccostrano = dataFrameTransactions330291_388158['hashBlock'].values[0]
print(bloccostrano)

takeFistRow = takeFistRow.append(dataFrameTransactions330291_388158_MAX)
print(takeFistRow)
print("-----------------------")



##### ---------------------------------- #####


fileCsvTransactions388159_446026 = pd.read_csv('T:\\file_csv_tesi\\transactions-388159_446026.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions388159_446026 = pd.DataFrame(fileCsvTransactions388159_446026.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions388159_446026 = dataFrameTransactions388159_446026.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions388159_446026_MAX = pd.DataFrame({"hashblock": dataFrameTransactions388159_446026['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions388159_446026['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions388159_446026_MAX)
print(takeFistRow)
print("-----------------------")

##### ---------------------------------- #####

fileCsvTransactions446027_473988 = pd.read_csv('T:\\file_csv_tesi\\transactions-446027_473988.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions446027_473988 = pd.DataFrame(fileCsvTransactions446027_473988.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions446027_473988 = dataFrameTransactions446027_473988.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions446027_473988_MAX = pd.DataFrame({"hashblock": dataFrameTransactions446027_473988['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions446027_473988['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions446027_473988_MAX)
print(takeFistRow)
print("-----------------------")

##### ---------------------------------- #####

fileCsvTransactions473989_501950 = pd.read_csv('T:\\file_csv_tesi\\transactions-473989_501950.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions473989_501950 = pd.DataFrame(fileCsvTransactions473989_501950.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions473989_501950 = dataFrameTransactions473989_501950.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions473989_501950_MAX = pd.DataFrame({"hashblock": dataFrameTransactions473989_501950['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions473989_501950['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions473989_501950_MAX)
print(takeFistRow)
print("-----------------------")

##### ---------------------------------- #####

fileCsvTransactions501951_529133 = pd.read_csv('T:\\file_csv_tesi\\transactions-501951_529133.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions501951_529133 = pd.DataFrame(fileCsvTransactions501951_529133.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions501951_529133 = dataFrameTransactions501951_529133.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions501951_529133_MAX = pd.DataFrame({"hashblock": dataFrameTransactions501951_529133['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions501951_529133['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions501951_529133_MAX)
print(takeFistRow)
print("-----------------------")
##### ---------------------------------- #####


fileCsvTransactions529134_556315 = pd.read_csv('T:\\file_csv_tesi\\transactions-529134_556315.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions529134_556315 = pd.DataFrame(fileCsvTransactions529134_556315.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions529134_556315 = dataFrameTransactions529134_556315.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions529134_556315_MAX = pd.DataFrame({"hashblock": dataFrameTransactions529134_556315['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions529134_556315['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions529134_556315_MAX)
print(takeFistRow)
print("-----------------------")

fileCsvTransactions556316_583500  = pd.read_csv('T:\\file_csv_tesi\\transactions-556316_583500.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions556316_583500 = pd.DataFrame(fileCsvTransactions556316_583500.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions556316_583500 = dataFrameTransactions556316_583500.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions556316_583500_MAX = pd.DataFrame({"hashblock": dataFrameTransactions556316_583500['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions556316_583500['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions556316_583500_MAX)
print(takeFistRow)
print("-----------------------")

##### ---------------------------------- #####

fileCsvTransactions583501_610680 = pd.read_csv('T:\\file_csv_tesi\\transactions-583501_610680.csv', sep=";", names = ["txid", "hashBlock", "version", "lockTime"])
dataFrameTransactions583501_610680 = pd.DataFrame(fileCsvTransactions583501_610680.value_counts(subset=["hashBlock"])).reset_index()
dataFrameTransactions583501_610680 = dataFrameTransactions583501_610680.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
dataFrameTransactions583501_610680_MAX = pd.DataFrame({"hashblock": dataFrameTransactions583501_610680['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions583501_610680['Valore_massimo'].values[0]]})

takeFistRow = takeFistRow.append(dataFrameTransactions583501_610680_MAX)
print(takeFistRow)
print("-----------------------")

##### ---------------------------------- #####

print("ORDINATO: ")
takeFistRow = takeFistRow.sort_values(by=['Valore_massimo'], ascending=False)
print(takeFistRow)

print("Questo è il blockhash del blocco con più transazioni: ")
print(takeFistRow['hashblock'].values[0])


############ RICERCA BLOCKHASH ##################
print("Ricerca BLOCKHASH:")
block_hash_trovato = takeFistRow['hashblock'].values[0]
print(block_hash_trovato)
fileCsvBlocks0_214553 = pd.read_csv('T:\\file_csv_tesi\\blocks-0_214553.csv', sep=";")
fileCsvBlocks214554_272422 = pd.read_csv('T:\\file_csv_tesi\\blocks-214554_272422.csv', sep=";")
fileCsvBlocks272423_330290 = pd.read_csv('T:\\file_csv_tesi\\blocks-272423_330290.csv', sep=";")
fileCsvBlocks330291_388158 = pd.read_csv('T:\\file_csv_tesi\\blocks-330291_388158.csv', sep=";")
fileCsvBlocks388159_446026 = pd.read_csv('T:\\file_csv_tesi\\blocks-388159_446026.csv', sep=";")
fileCsvBlocks446027_473988 = pd.read_csv('T:\\file_csv_tesi\\blocks-446027_473988.csv', sep=";")
fileCsvBlocks473989_501950 = pd.read_csv('T:\\file_csv_tesi\\blocks-473989_501950.csv', sep=";")
fileCsvBlocks501951_556315 = pd.read_csv('T:\\file_csv_tesi\\blocks-501951_556315.csv', sep=";")
fileCsvBlocks556316_610680 = pd.read_csv('T:\\file_csv_tesi\\blocks-556316_610680.csv', sep=";")

i = 0

for i in range(len(fileCsvBlocks0_214553)):
    if block_hash_trovato == fileCsvBlocks0_214553.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks0_214553['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks214554_272422)):
    if block_hash_trovato == fileCsvBlocks214554_272422.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks214554_272422['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks272423_330290)):
    if block_hash_trovato == fileCsvBlocks272423_330290.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks272423_330290['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks330291_388158)):
    if block_hash_trovato == fileCsvBlocks330291_388158.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks330291_388158['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks388159_446026)):
    if block_hash_trovato == fileCsvBlocks388159_446026.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks388159_446026['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks446027_473988)):
    if block_hash_trovato == fileCsvBlocks446027_473988.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks446027_473988['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks473989_501950)):
    if block_hash_trovato == fileCsvBlocks473989_501950.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks473989_501950['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks501951_556315)):
    if block_hash_trovato == fileCsvBlocks501951_556315.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks501951_556315['nTime'].values[i]
        break

for i in range(len(fileCsvBlocks556316_610680)):
    if block_hash_trovato == fileCsvBlocks556316_610680.block_hash[i]:
        nTime_Che_Cerco = fileCsvBlocks556316_610680['nTime'].values[i]
        break



print("questo + il block hash")
print(block_hash_trovato)
print("questo il tempo")
print(nTime_Che_Cerco)

###ORA LO CONVERTO

datetime_object = datetime.fromtimestamp(nTime_Che_Cerco)
print("DATA DEL BLOCCO CON PIù TRANSAZIONI:", datetime_object)
