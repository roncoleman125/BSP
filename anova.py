import pandas as pd
from scipy import stats
import numpy as np

# Load in the file
# RESULTS = "/users/roncoleman/tmp/style/results.txt"
DIR = "/users/roncoleman/GD/marist/research/better-style/results/"

# Pairs
# RESULTS="allegro5-kr-orig-jac-gindent-10.txt" # ** statistically significant
# RESULTS="allegro5-kr-linux-jac-gindent-10.txt"
# RESULTS="allegro5-kr-gnu-jac-gindent-10.txt"
# RESULTS="allegro5-orig-gnu-jac-gindent-10.txt"
# RESULTS="allegro5-linux-gnu-jac-gindent-10.txt"
RESULTS="allegro5-linux-orig-jac-gindent-10.txt"

# Triples
RESULTS="allegro5-kr-orig-linux-jac-gindent-10.txt"  # KBL
RESULTS="allegro5-kr-orig-gnu-jac-gindent-10.txt"    # KBG
RESULTS="allegro5-kr-linux-gnu-jac-gindent-10.txt"   # KLG
RESULTS="allegro5-orig-linux-gnu-jac-gindent-10.txt" # BLG

# Quadruple
RESULTS="allegro5-kr-orig-linux-gnu-jac-gindent-10.txt" # KBLG

df = pd.read_csv(DIR+RESULTS, delimiter=r"\s+")

# Round to three places
STYLES = ['kr', 'linux', 'orig', 'gnu']

# print(df['orig:cos'].median())
# print(df['gnu:cos'].median())

df_t = pd.DataFrame()

# for style in STYLES:
#     key = style + ':cos'
#     key_t = style + "_cos"
#     df_t[key_t] = df[key] #.apply(lambda p: round(p,2))

# gains = df_t[df_t.orig_cos >= df_t.gnu_cos  ]
#
# print(len(gains))

########
# https://medium.com/datadriveninvestor/finding-outliers-in-dataset-using-python-efc3fce6ce32
# print(stats.normaltest(df_t['kr_cos']))
#
# q1, q3 = np.percentile(df_t['kr_cos'],[25, 75])
#
# iqr = q3 - q1
#
# lower_bound = q1 -(1.5 * iqr)
# upper_bound = q3 +(1.5 * iqr)
#
# print("lower bound: %f upper bound: %f" %(lower_bound, upper_bound))
#
# df_f = pd.DataFrame()
#
# df_f = df_t[df_t.kr_cos >= lower_bound][df_t.kr_cos <= upper_bound]
#
# print(len(df_f))
# print(stats.normaltest(df_f['kr_cos']))

# q1, q3 = np.percentile(df_t['linux_cos'],[25, 75])
#
# iqr = q3 - q1
#
# lower_bound = q1 -(1.5 * iqr)
# upper_bound = q3 +(1.5 * iqr)
#
# df_f = pd.DataFrame()
# df_f = df_t[df_t.linux_cos >= lower_bound][df_t.linux_cos <= upper_bound]
#
# print(len(df_f))
# print(stats.normaltest(df_f['linux_cos']))

############
# print(stats.wilcoxon(df_t['orig_cos'], df_t['linux_cos']))

# print("kr vs gnu: "+str(stats.wilcoxon(df_t['kr_cos'], df_t['gnu_cos'])))

print(RESULTS+": "+str(df.shape))

# https://astatsa.com/OneWay_Anova_with_TukeyHSD/
# print("H test cos: "+str(stats.kruskal(df_t['kr_cos'], df_t['linux_cos'], df_t['orig_cos'], df_t['gnu_cos'])))
#
# seen = []
# for style1 in STYLES:
#     for style2 in STYLES:
#         if style1 == style2:
#             continue
#         seeing_a = style1 + style2
#         seeing_b = style2 + style1
#         if seeing_a in seen or seeing_b in seen:
#             continue
#         seen.append(seeing_a)
#         print(style1 + " vs "+style2 +": "+str(stats.wilcoxon(df_t[style1+"_cos"], df_t[style2+"_cos"])))


# for style in STYLES:
#     print(style+" cos median: " + str(np.median(df_t[style + '_cos'])))
# print()

df_t = pd.DataFrame()

for style in STYLES:
    key = style + ':d'
    key_t = style + "_d"
    df_t[key_t] = df[key] / df["base:loc"]

print("H test d: "+str(stats.kruskal(df['kr:d'], df['linux:d'], df['orig:d'], df['gnu:d'])))


# for style in STYLES:
#     # print("median "+style+": "+str(np.median(df_t[style+'_cos'])))
#     print(style+" d percentiles: "+str(np.percentile(df_t[style+"_d"],[25, 50, 75, 95])))
seen = []
for style1 in STYLES:
    for style2 in STYLES:
        if style1 == style2:
            continue
        seeing_a = style1 + style2
        seeing_b = style2 + style1
        if seeing_a in seen or seeing_b in seen:
            continue
        seen.append(seeing_a)
        print(style1 + " vs "+style2 +" d: "+str(stats.wilcoxon(df[style1+":d"], df[style2+":d"])))
for style in STYLES:
    print(style + " d median: " + str(np.median(df[style + ':d'])))
print()

print("H test _d: "+str(stats.kruskal(df_t['kr_d'], df_t['linux_d'], df_t['orig_d'], df_t['gnu_d'])))

seen = []
for style1 in STYLES:
    for style2 in STYLES:
        if style1 == style2:
            continue
        seeing_a = style1 + style2
        seeing_b = style2 + style1
        if seeing_a in seen or seeing_b in seen:
            continue
        seen.append(seeing_a)
        print(style1 + " vs "+style2 +" _d: "+str(stats.wilcoxon(df_t[style1+"_d"], df_t[style2+"_d"])))

for style in STYLES:
    print(style + " _d median: " + str(np.median(df_t[style + '_d'])))

# for style in STYLES:
#     print(style + " _d normal: " + str(stats.normaltest(df_t[style+"_d"])))