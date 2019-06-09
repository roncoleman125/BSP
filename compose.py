import pandas as pd
from scipy import stats
import numpy as np

DIR = "/users/roncoleman/GD/marist/research/better-style/results/"
SUFFIX = "-jac-gindent-10.txt"
REPOS = "coreutils"
STYLES = ["kr", "orig", "linux", "gnu"]
COMPOSING = ["kr", "linux"]
DECOMPOSING = ["orig", "gnu"]

# RESULTS="coreutils-kr-linux-jac-gindent-10.txt"


composite = pd.DataFrame()

for compose in COMPOSING:
    name = REPOS + "-" + compose + SUFFIX

    path = DIR + name

    df = pd.read_csv(path, delimiter=r"\s+")

    # key = compose + ":d"
    # composite[key]= df[key]

    for style in STYLES:
        key = style + ":d"

        if key in composite.columns:
            composite[key] = (composite[key] + df[key]) / 2
        else:
            composite[key] = df[key]

print(str(COMPOSING)+": "+str(composite.shape))

print(composite)

# https://astatsa.com/OneWay_Anova_with_TukeyHSD/
print("H test cos: "+str(stats.kruskal(composite['kr:d'], composite['linux:d'], composite['orig:d'], composite['gnu:d'])))

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
        print(style1 + " vs "+style2 +": "+str(stats.wilcoxon(composite[style1+":d"], composite[style2+":d"])))

for style in STYLES:
    print(style + " d median: " + str(np.median(composite[style + ':d'])))
