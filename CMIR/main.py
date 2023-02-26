from collections import Counter
import matplotlib.pyplot as plt
from math import log10
#returns list of words in sentence without tag
def parse_word(sentence: str):
    new_sentence = []
    tags = []

    tokenized = sentence.split()
    for word in tokenized:
        new_word  = ""
        tag = ""
        for ch in word:
            if not ch.isupper():
                new_word+=ch
            else:
                tag+=ch
        new_sentence.append(new_word)
        tags.append(tag)
    return new_sentence, tags

f = open('new_data_language_tagged_combined.txt', 'r')
# g = open('untagged.txt', 'w')
# h = open('tagged_data.txt', 'w')
# for x in f:
#     g.write(' '.join(parse_word(x)[0]) + '\n')
#     parsed = parse_word(x)
#     for i in range(len(parsed[0])):
#         h.write(parsed[0][i] + '\t' + parsed[1][i] + '\n')
#     h.write('\n')

#     # h.write(str(parse_word(x)[1]) + '\n')

# f.close()
# g.close()
# h.close()


# rank vs freq
ind = Counter()
s = set()

for x in f:
    parsed = parse_word(x)
    ind.update(parsed[0])
    for k in parsed[1]:
        s.add(k)
print(s)
print(ind.most_common(10))

frequency = []
for x in ind.most_common():
    frequency.append(log10(x[1]))
rank = []

for i, _ in enumerate(frequency):
    rank.append(log10(i+1))

plt.plot(rank,frequency)
plt.xlabel("log(rank)")
plt.ylabel("log(frequency)")
# plt.savefig("rankvsfreq.png")
plt.show()

s = open('stopwords.txt', 'w')
num = 500
for i in ind:
    if ind[i] > num:
        s.write(i + '\n')
