import pandas as pd
from scipy import stats
import numpy as np

# Load in the file
# RESULTS = "/users/roncoleman/tmp/style/results.txt"
DIR = "/users/roncoleman/GD/marist/research/better-style/results/"

# RESULTS = "linux-kernel-styles-cos-gindent-nograte.txt"
RESULTS = "linux-kernel-styles-cos-gindent.txt"
df = pd.read_csv(DIR+RESULTS, delimiter=r"\s+")

# Round to three places
STYLES = ['kr', 'linux', 'orig', 'gnu']

df_t = pd.DataFrame()

for style in STYLES:
    key = style + ':cos'
    key_t = style + "_cos"
    df_t[key_t] = df[key].apply(lambda p: round(p,2))

for style in STYLES:
    key = style + ":loc"
    key_t = style + "_loc"
    df_t[key_t] = df[key]

for style in STYLES:
    key = style + '_cos'
    print(df_t[key].value_counts())

print(stats.kruskal(df_t['kr_cos'], df_t['linux_cos'], df_t['orig_cos'], df_t['gnu_cos']))

gains = df_t[df_t.linux_cos >= df_t.gnu_cos  ]

print(len(gains))

print(np.corrcoef(df_t['kr_cos'],df_t['kr_loc']))