import pandas as pd
import scipy.stats as stats

# RESULTS = "/users/roncoleman/tmp/style/results.txt"
DIR = "/users/roncoleman/GD/marist/research/jcsit2019/"

RESULTS = "results-coreutils.xlsx"
df = pd.read_excel(DIR+RESULTS, sheet_name='Sheet1')

print(df['BF(GNU)'].median())
print(df['BF(Linux)'].median())
print(df['BF(K&R)'].median())
print(df['BF(Berkeley)'].median())