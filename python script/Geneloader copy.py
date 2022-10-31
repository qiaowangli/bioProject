#!/Users/royli/miniforge3/bin/python3

import os
import pandas as pd

""" Global Variable """
path = '/Users/royli/Desktop/TCGA_PRAD'
dfList = []

def parser(userId, tsvfile):
    buffer = pd.read_table(tsvfile, skiprows=1)
    userID_col = pd.DataFrame([userId]*len(buffer))
    buffer.insert (0, 'patient_id', userID_col)
    dfList.append(buffer)
    print(len(dfList))


def loader():
    tcgaFolder = os.listdir(path)
    for folder in tcgaFolder:
        if(os.path.isdir(path+'/'+folder)):
            tcgaFile = os.listdir(path+'/'+folder)
            for file in tcgaFile:
                if(file.split('.')[-1]=='tsv'):
                    parser(file.split('.rna_seq.augmented_star_gene_counts')[0], path+'/'+folder+ '/'+file)

loader()
result = pd.concat(dfList)
result.to_csv('allData.csv', index=False)
                

