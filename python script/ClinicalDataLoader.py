#!/Users/royli/miniforge3/bin/python3

import json
from nis import cat
import pandas as pd

# create an Empty DataFrame object
df = pd.DataFrame(columns = ['CASE_ID','treatment_type','days_to_last_follow_up','days_to_death', 'age_at_diagnosis','year_of_diagnosis',
                            'race','gender','ethnicity','vital_status','age_at_index','year_of_death'])

# Opening JSON file
f = open('/Users/royli/Desktop/TCGA_PRAD_DATA/clinical.cart.2022-10-27.json')

data = json.load(f)
for dataObject in data:
    try:

        df=df.append(
        {
        'CASE_ID' : dataObject['case_id'],
        'treatment_type' : dataObject['diagnoses'][0]['treatments'][0]['treatment_type'],
        'days_to_last_follow_up' : dataObject['diagnoses'][0]['days_to_last_follow_up'],
        'days_to_death' : dataObject['demographic']['days_to_death'],
        'age_at_diagnosis' : dataObject['diagnoses'][0]['age_at_diagnosis'],
        'year_of_diagnosis' : dataObject['diagnoses'][0]['year_of_diagnosis'],
        'race' : dataObject['demographic']['race'],
        'gender' : dataObject['demographic']['gender'],
        'ethnicity' : dataObject['demographic']['ethnicity'],
        'vital_status' : dataObject['demographic']['vital_status'],
        'age_at_index' : dataObject['demographic']['age_at_index'],
        'year_of_death' : dataObject['demographic']['year_of_death']
        },
        ignore_index= True)
    except: 
        df=df.append(
            {
            'CASE_ID' : dataObject['case_id'],
            'treatment_type' : dataObject['diagnoses'][0]['treatments'][0]['treatment_type'],
            'days_to_last_follow_up' : dataObject['diagnoses'][0]['days_to_last_follow_up'],
            'days_to_death' : -1,
            'age_at_diagnosis' : dataObject['diagnoses'][0]['age_at_diagnosis'],
            'year_of_diagnosis' : dataObject['diagnoses'][0]['year_of_diagnosis'],
            'race' : dataObject['demographic']['race'],
            'gender' : dataObject['demographic']['gender'],
            'ethnicity' : dataObject['demographic']['ethnicity'],
            'vital_status' : dataObject['demographic']['vital_status'],
            'age_at_index' : dataObject['demographic']['age_at_index'],
            'year_of_death' : dataObject['demographic']['year_of_death']
            
            },
            ignore_index= True)
df.to_csv('ClinicalData.csv',index = False)


