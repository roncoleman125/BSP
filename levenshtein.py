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
# RESULTS = "gimp-styles-cos-gindent.txt"
# RESULTS = "mysql-styles-cos-gindent.txt"
RESULTS = "allegro5-styles-cos-gindent.txt"


df = pd.read_csv(DIR+RESULTS, delimiter=r"\s+")

# Round to three places
STYLES = ['kr', 'linux', 'orig', 'gnu']


df_t = pd.DataFrame()

for style in STYLES:
    key = style + ':d'
    key_t = style + "_d"
    df_t[key_t] = df[key] / df ["base:loc"]

for style in STYLES:
    print("median "+style+": "+str(np.median(df_t[style+'_d'])))


