# bioProject

## Step 1: 

The raw data should be obtained throught the TCGA link.

## Step 2: 

If you download the gene data, You will get a folder with many subfolders, where each subfolder stores the genetic data of one patient(use Geneloader.py and update the path of that folder)

If you download the clinical/meta data, use(ClinicalDataLoader.py/UserIdLoader.py and update the path of that folder)

## Step 3: 

Use the docker-compose.yml file to generate a PgSQL container and import all the csv file to DBMS