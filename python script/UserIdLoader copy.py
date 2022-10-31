#!/Users/royli/miniforge3/bin/python3

import json
import pandas as pd

# create an Empty DataFrame object
df = pd.DataFrame(columns = ['TCGA_ID', 'CASE_ID','PATIENT_ID'])

# Opening JSON file
f = open('/Users/royli/Desktop/TCGA_PRAD_DATA/metadata.cart.2022-10-26.json')

data = json.load(f)
print(data[0]['file_name'].split('.rna_seq.augmented_star_gene_counts')[0])
print(data[0]['associated_entities'][0]['entity_submitter_id'])

for dataObject in data:
    df=df.append(
        {
        'TCGA_ID' : dataObject['associated_entities'][0]['entity_submitter_id'],
        'CASE_ID' : dataObject['associated_entities'][0]['case_id'],
        'PATIENT_ID' : dataObject['file_name'].split('.rna_seq.augmented_star_gene_counts')[0]
        },
        ignore_index= True)
df.to_csv('NewIdData.csv',index = False)


