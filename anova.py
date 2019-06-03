import pandas as pd
from scipy import stats
import numpy as np

# Load in the file
# RESULTS = "/users/roncoleman/tmp/style/results.txt"
DIR = "/users/roncoleman/GD/marist/research/better-style/results/"

# RESULTS = "linux-kernel-styles-cos-gindent-nograte.txt"
# RESULTS = "linux-kernel-styles-cos-gindent.txt"
# RESULTS = "linux-lib-styles-cos-gindent.txt"
# RESULTS = "coreutils-styles-cos-gindent.txt"
# RESULTS = "gmp-styles-cos-gindent.txt"
#RESULTS = "gimp-styles-cos-gindent.txt"
# RESULTS = "mysql-styles-cos-gindent.txt"
RESULTS = "allegro5-styles-cos-gindent.txt"


df = pd.read_csv(DIR+RESULTS, delimiter=r"\s+")

# Round to three places
STYLES = ['kr', 'linux', 'orig', 'gnu']

# print(df['orig:cos'].median())
# print(df['gnu:cos'].median())

df_t = pd.DataFrame()

for style in STYLES:
    key = style + ':cos'
    key_t = style + "_cos"
    df_t[key_t] = df[key] #.apply(lambda p: round(p,2))

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
print("H test: "+str(stats.kruskal(df_t['kr_cos'], df_t['linux_cos'], df_t['orig_cos'], df_t['gnu_cos'])))

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
        print(style1 + " vs "+style2 +": "+str(stats.wilcoxon(df_t[style1+"_cos"], df_t[style2+"_cos"])))

for style in STYLES:
    # print("median "+style+": "+str(np.median(df_t[style+'_cos'])))
    print(style+" percentiles: "+str(np.percentile(df_t[style+"_cos"],[25, 50, 75, 95])))