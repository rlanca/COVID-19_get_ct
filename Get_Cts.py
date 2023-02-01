import pandas as pd
import numpy as np 
import glob
import os

a = (input("Enter the path to the working directory: "))
os.chdir(a)

all_filenames = [i for i in glob.glob('*.csv')]

df = pd.concat([pd.read_csv(f, skiprows = 12) for f in all_filenames], ignore_index=True)
df.reset_index(drop=True)
filt = (
    (df['Sample Name'] == 'PC') | 
    (df['Sample Name'] == 'PC1') |
    (df['Sample Name'] == 'PC2') |
    (df['Sample Name'] == 'PC-1') |
    (df['Sample Name'] == 'PC-2') |
    (df['Sample Name'] == 'pc1') |
    (df['Sample Name'] == 'pc2') |
    (df['Sample Name'] == 'NC') | 
    (df['Sample Name'] == 'NC2') |
    (df['Sample Name'] == 'NC-1') | 
    (df['Sample Name'] == 'NC-2') | 
    (df['Sample Name'] == 'NC-3')
    )

df = df[filt]
df = df[['Batch ID', 'Sample Name', 'ORF1ab Ct', 'N gene Ct', 'S gene Ct', 'MS2 Ct']]

ORF1ab = list(df["ORF1ab Ct"])
ORF1ab = [ct for ct in ORF1ab if not(pd.isnull(ct)) == True]
print("ORF1ab", ORF1ab)

Ngene = list(df["N gene Ct"])
Ngene = [ct for ct in Ngene if not(pd.isnull(ct)) == True]
print("Ngene", Ngene)

Sgene = list(df["S gene Ct"])
Sgene = [ct for ct in Sgene if not(pd.isnull(ct)) == True]
print("Sgene", Sgene)

MS2 = list(df["MS2 Ct"])
MS2 = [ct for ct in MS2 if not(pd.isnull(ct)) == True]
print("MS2", MS2)
