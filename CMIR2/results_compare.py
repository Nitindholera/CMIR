import pandas as pd
import matplotlib.pylab as plt
import os
files = []
path = 'results/only_stopwords/bn_and_english/tfidf/'
with os.scandir(path) as entries:
    for x in entries:
        files.append(x.name)
print(files)
x = []
y = []
for f in files:
    df = pd.read_csv(os.path.join(path, f))
    y.append(df.iloc[1,2])
    x.append(f)

# plt.plot(x, y)
# plt.savefig('res_df.png')
# plt.show()
print(max(y))
print(x[y.index(max(y))])