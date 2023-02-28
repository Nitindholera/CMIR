import pandas as pd
import matplotlib.pylab as plt
import os
import numpy as np
import seaborn as sns

files = []
path = 'results/only_stopwords/bn_and_english/tfidf/'
with os.scandir(path) as entries:
    for x in entries:
        files.append(x.name)
print(files)
x = np.zeros((9,9))
y = []
# for f in files:
#     if os.path.isfile(os.path.join(path, f)):
#         df = pd.read_csv(os.path.join(path, f))
#         i = 0
#         j = 0
#         x[i][j] = df.iloc[1,2]
#         # y.append(df.iloc[1,2])
#         print(f)
# 6 10
# 5.2 - 6.8
# 9.2 - 10.8
num1 = 0
num2 = 0
for i in range(52,70, 2):
    for j in range(92,110, 2):
        f = f"{i//10}.{i%10}_{j//10}.{j%10}.csv"
        # print(f)
        df = pd.read_csv(os.path.join(path, f))
        x[num1][num2] = df.iloc[1,2]
        # print(num1, num2)
        num2+=1
    num1+=1
    num2 = 0
# print(x)
plt.imshow(x, interpolation='nearest', extent=[9.2,11.8,6.8,5.2])
# plt.xlim(1,15)
# plt.ylim(1,15)
plt.xlabel('Bengali_threshold')
plt.ylabel('English_threshold')
plt.savefig('fig.png')
plt.show()
# print(x[6-1][10-1])
# y = [i for i in range(15)]*15
# df_x = pd.DataFrame({'MutProb': y, 'Bn_val': y, 'value': x.flatten()})
# result = df.pivot(index='Eng_val', columns='Bn_val', values='value')
# sns.heatmap(result, annot=True, fmt="g", cmap='viridis')

# plt.plot(x, y)
# plt.savefig('res_df.png')
# plt.show()
# print(max(y))
# print(x[y.index(max(y))])


# load the sample data
# df = pd.DataFrame({'MutProb': [0.1,
#   0.05, 0.01, 0.005, 0.001, 0.1, 0.05, 0.01, 0.005, 0.001, 0.1, 0.05, 0.01, 0.005, 0.001, 0.1, 0.05, 0.01, 0.005, 0.001, 0.1, 0.05, 0.01, 0.005, 0.001], 'SymmetricDivision': [1.0, 1.0, 1.0, 1.0, 1.0, 0.8, 0.8, 0.8, 0.8, 0.8, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2, 0.2, 0.2, 0.2, 0.2], 'test': ['sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule', 'sackin_yule'], 'value': [-4.1808639999999997, -9.1753490000000006, -11.408113999999999, -10.50245, -8.0274750000000008, -0.72260200000000008, -6.9963940000000004, -10.536339999999999, -9.5440649999999998, -7.1964070000000007, -0.39225599999999999, -6.6216390000000001, -9.5518009999999993, -9.2924690000000005, -6.7605589999999998, -0.65214700000000003, -6.8852289999999989, -9.4557760000000002, -8.9364629999999998, -6.4736289999999999, -0.96481800000000006, -6.051482, -9.7846860000000007, -8.5710630000000005, -6.1461209999999999]})

# # pivot the dataframe from long to wide form
# result = df.pivot(index='SymmetricDivision', columns='MutProb', values='value')

# sns.heatmap(result, annot=True, fmt="g", cmap='viridis')
# plt.show()