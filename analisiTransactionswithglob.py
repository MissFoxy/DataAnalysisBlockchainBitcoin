import pandas as pd
import os
import glob
from datetime import datetime

takeFistRow = pd.DataFrame({"hashblock": [0], "Valore_massimo": [0] })

pathTransactions = "T:\\file_csv_tesi\\transactions\\"
csv_files_transactions = glob.glob(os.path.join(pathTransactions, "*.csv"))

for fileTransactions in csv_files_transactions:
    # read the csv file
    fileCsvTransactions = pd.read_csv(fileTransactions, sep = ";", names = ["txid", "hashBlock", "version", "lockTime"])
    dataFrameTransactions = pd.DataFrame(fileCsvTransactions.value_counts(subset=["hashBlock"])).reset_index()
    dataFrameTransactions = dataFrameTransactions.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)
    dataFrameTransactions_MAX = pd.DataFrame({"hashblock": dataFrameTransactions['hashBlock'].values[0], "Valore_massimo": [dataFrameTransactions['Valore_massimo'].values[0]]})

    #print("dataframe:")
    #print(dataFrameTransactions.head(3))
    takeFistRow = takeFistRow.append(dataFrameTransactions_MAX)

    # print the location and filename
    print('File location:', fileTransactions)
    print('File Name:', fileTransactions.split("\\")[-1])

    print(takeFistRow)

    print("-----------------------")

    # print the location and filename
    print('File location:', fileTransactions)
    print('File Name:', fileTransactions.split("\\")[-1])

    # print the content
    print('Content:')
    print(fileCsvTransactions)
    

##### ---------------------------------- #####
#ordinandoli:
takeFistRow = takeFistRow.sort_values(by=['Valore_massimo'], ascending=False)

print(takeFistRow['hashblock'].values[0])


############ RICERCA BLOCKHASH ##################
block_hash_trovato = takeFistRow['hashblock'].values[0]
print("Questo è il blockhash del blocco con più transazioni: ")
print(block_hash_trovato)
#print("Ricerca BLOCKHASH:")
pathBlocks = "T:\\file_csv_tesi\\blocks_2\\"
csv_files_blocks = glob.glob(os.path.join(pathBlocks, "*.csv"))
#block_hash_trovato = "00000000000000001080e6de32add416cd6cda29f35ec9bce694fea4b964c7be" #mi serve a testare il secondo for senza eseguire il primo
i = 0
nTime_blocco = 0

for fileBlocks in csv_files_blocks:
    fileCsvBlocks = pd.read_csv(fileBlocks, sep=";", names=["block_hash","height","version","blocksize","hashPrev","hashMerkleRoot","nTime","nBits","nNonce"],  low_memory=False) # low_memory=False messo perché me l'ha detto la console
    #print('File location:', fileBlocks)
    #print('File Name:', fileBlocks.split("\\")[-1])
    for i in range(len(fileCsvBlocks)):

        if fileCsvBlocks['block_hash'].values[i] == block_hash_trovato:
            #print(fileCsvBlocks['nTime'].values[i])
            nTime_blocco = fileCsvBlocks['nTime'].values[i]
            break
    if (nTime_blocco != 0):
        break

#print(type(nTime_blocco))
#--------------converto il valore in int-------------#
nTime_blocco_converted = int(nTime_blocco)
#print(type(nTime_blocco_converted))
print("In UNIX il valore è: "+ nTime_blocco)
###ORA LO CONVERTO
datetime_object = datetime.fromtimestamp(nTime_blocco_converted)
print("Data del blocco con più transazioni: ", datetime_object)