import pandas as pd
import os
import glob
from datetime import datetime

takeFistRow = [{"hashblock": "stringa", "Valore_massimo": 0}]


pathTransactions = "L:\\TESI\\transactions\\"
csv_files_transactions = glob.glob(os.path.join(pathTransactions, "*.csv"))

tx_in_media = []

for fileTransactions in csv_files_transactions:
    fileCsvTransactions = pd.read_csv(fileTransactions, sep=";", names=["txid", "hashBlock", "version", "lockTime"])
    dataFrameTransactions = pd.DataFrame(fileCsvTransactions.value_counts(subset=["hashBlock"])).reset_index()
    dataFrameTransactions = dataFrameTransactions.set_axis(['hashBlock', 'Valore_massimo'], axis=1, inplace=False)

    print("quante transazioni sono", len(fileCsvTransactions))
    print(("numero blocchi "), len(dataFrameTransactions))
    print("media: ", len(fileCsvTransactions)/len(dataFrameTransactions))
    tx_in_media.append(len(fileCsvTransactions)/len(dataFrameTransactions))
    print("tx_in_media", tx_in_media)

    valore_massimo = int(dataFrameTransactions['Valore_massimo'].values[0])
    hashBlock = str(dataFrameTransactions['hashBlock'].values[0])
    takeFistRow.append({"hashBlock": hashBlock, "Valore_massimo": valore_massimo})
    print(takeFistRow)


tx_in_media = pd.DataFrame(tx_in_media)
print(tx_in_media)
tx_in_media_globale = tx_in_media / len(tx_in_media)
print("media globale: ", tx_in_media_globale)

#cerco il blocco
pathBlocks = "T:\\file_csv_tesi\\blocks_2\\"
csv_files_blocks = glob.glob(os.path.join(pathBlocks, "*.csv"))
i = 0
nTime_blocco = 0
quantiBlocchi = 0

for fileBlocks in csv_files_blocks:
    fileCsvBlocks = pd.read_csv(fileBlocks, sep=";", names=["block_hash", "height", "version", "blocksize", "hashPrev", "hashMerkleRoot", "nTime", "nBits", "nNonce"], low_memory=False)  # low_memory=False messo perché me l'ha detto la console

    quantiBlocchi = quantiBlocchi + len(fileCsvBlocks)

    for i in range(0, len(fileCsvBlocks), 1):

        if fileCsvBlocks['block_hash'].values[i] == block_hash_trovato:
            # print(fileCsvBlocks['nTime'].values[i])
            nTime_blocco = fileCsvBlocks['nTime'].values[i]
            break
    if (nTime_blocco != 0):
        break

# --------------converto il valore in int-------------#
nTime_blocco_converted = int(nTime_blocco)
print("**----------------------------------------------------------------------**")
print("In UNIX il valore è: ", nTime_blocco)
###ORA LO CONVERTO
datetime_object = datetime.fromtimestamp(nTime_blocco_converted)
print("Data del blocco con più transazioni: ", datetime_object)

numMedioTransazioni = sommaTransazioni / quantiBlocchi
print("I blocchi hanno in media questo numero di transazioni: ", numMedioTransazioni)
print("**----------------------------------------------------------------------**")
