import pandas as pd
import scipy.stats as stats

# RESULTS = "/users/roncoleman/tmp/style/results.txt"
DIR = "/users/roncoleman/GD/marist/research/jcsit2019/"

RESULTS = "results-coreutils.xlsx"
df = pd.read_excel(DIR+RESULTS, sheet_name='Sheet1')


result = stats.kruskal(df['BF(GNU)'], df['BF(K&R)'], df['BF(Berkeley)'], df['BF(Linux)'])
print("beauty: "+str(result))

result = stats.kruskal(df['mioh'], df['mims'], df['misei'])
print ("maintainability: "+str(result))

# result = stats.spearmanr(df['BF(GNU)'],df['mioh'])
# print("GNU vs. OH: "+str(result))

STYLES = ["GNU", "Linux", "K&R" ,"Berkeley"]
LABELS = { "GNU": "GNU", "K&R":"K&R", "Berkeley": "BSD", "Linux": "LIN"}
MIS = ["oh", "sei", "ms"]

print("correlations:")
print("T   ", end=' ')
for mi in MIS:
    print("%3s " % (mi.upper()), end=' ')

print(" ")

for style in STYLES:
    print(LABELS[style],end=' ')

    for mi in MIS:
        key1 = "BF(" + style + ")"

        key2 = "mi" + mi

        result = stats.spearmanr(df[key1], df[key2])
        # print(key1 +" vs. "+ key2 + ": "+str(result))
        print("%6.4f" % (result.correlation),end=' ')
    print(" ")

#########
print("pvalues:")
print("T   ", end=' ')
for mi in MIS:
    print("%3s " % (mi.upper()), end=' ')

print(" ")

for style in STYLES:
    print(LABELS[style],end=' ')

    for mi in MIS:
        key1 = "BF(" + style + ")"

        key2 = "mi" + mi

        result = stats.spearmanr(df[key1], df[key2])
        # print(key1 +" vs. "+ key2 + ": "+str(result))
        print("%4.2f" % (result.pvalue),end=' ')
    print(" ")

