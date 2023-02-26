import zipfile
import subprocess
from collections import Counter
import matplotlib.pyplot as plt
from math import log10
#returns list of words in sentence without tag
def parse_word(sentence: str):
    eng_sentence = []
    bn_sentence = []
    both = []

    tokenized = sentence.split()
    for word in tokenized:
        new_word  = ""

        tag = ""
        for ch in word:
            if not ch.isupper():
                new_word+=ch
            else:
                tag+=ch
        both.append(new_word)
        if tag == 'ENGLISH':
            eng_sentence.append(new_word)
        elif tag == 'BENGALI':
            bn_sentence.append(new_word)

    return eng_sentence, bn_sentence, both

def create_stopwords(val1,val2, mode):
    f = open(f'dataset/tagged/data.txt', 'r')
    
    indEng = Counter()
    indBn = Counter()
    combined_ind = Counter()
    ind_dict = dict()
    indEng_dict = dict()
    indBn_dict = dict()
    eng_words = 0
    Bn_words = 0
    for docid, x in enumerate(f):
        docid = docid + 1
        parsed = parse_word(x)
        indEng.update(parsed[0])
        indBn.update(parsed[1])
        combined_ind.update(parsed[2])
        
        for word in parsed[2]:
            if word in ind_dict.keys():
                if docid in ind_dict[word]:
                    ind_dict[word][docid] += 1
                else:
                    ind_dict[word][docid] = 1
            else:
                ind_dict[word] = dict({docid: 1})

        for word in parsed[0]:
            eng_words += 1
            if word in indEng_dict.keys():
                if docid in indEng_dict[word]:
                    indEng_dict[word][docid] += 1
                else:
                    indEng_dict[word][docid] = 1
            else:
                indEng_dict[word] = dict({docid: 1})

        for word in parsed[1]:
            Bn_words+=1
            if word in indBn_dict.keys():
                if docid in indBn_dict[word]:
                    indBn_dict[word][docid] += 1
                else:
                    indBn_dict[word][docid] = 1
            else:
                indBn_dict[word] = dict({docid: 1})

    s = open('stopword-list.txt', 'w')
    if mode == 'combined-tf':
        for i in combined_ind:
            if combined_ind[i] > val1:
                s.write(i+'\n')

    elif mode == 'combined-df':
        for i in ind_dict:
            if len(ind_dict[i]) > val1:
                s.write(i + '\n')

    elif mode == 'combined-normalised-tf':
        v = len(combined_ind)
        # gh = []
        for i in combined_ind:
            # gh.append(log10(v/combined_ind[i]))
            if log10(v/combined_ind[i]) < val1:
                s.write(i + '\n')
        # print(min(gh), max(gh))
    
    elif mode == 'combined-idf':
        n = 107900
        # gh = []
        for i in ind_dict:
            # gh.append(log10(n/len(ind_dict[i])))
            if log10(n/len(ind_dict[i])) < val1:
                s.write(i + '\n')
        # print(min(gh), max(gh))
    
    elif mode == 'combined-tfidf':
        n = 107900
        v = len(combined_ind)
        # gh = []
        for i in combined_ind:
            # gh.append(log10(v/combined_ind[i]) * log10(n/len(ind_dict[i])))
            if (log10(v/combined_ind[i]) * log10(n/len(ind_dict[i]))) < val1:
                s.write(i + '\n')
        # print(min(gh), max(gh))

    elif mode == 'bn_and_english-tf':
        for i in indEng:
            if indEng[i] > val1:
                s.write(i + '\n')
        for i in indBn:
            if indBn[i] > val2:
                s.write(i + '\n')

    
    elif mode == 'bn_and_english-df':
        for i in indEng:
            if len(indEng_dict[i]) > val1:
                s.write(i + '\n')
        for i in indBn:
            if len(indBn_dict[i]) > val2:
                s.write(i + '\n')
    
    elif mode == 'bn_and_english-normalised-tf':
        v = len(indEng)
        # g1 = []
        # g2 = []
        for i in indEng:
            # g1.append(log10(v/indEng[i]))
            if log10(v/indEng[i]) < val1:
                s.write(i + '\n')

        for i in indBn:
            # g2.append(log10(v/indBn[i]))
            if log10(v/indBn[i]) < val2:
                s.write(i + '\n')
        # print(min(g1), max(g1))
        # print(min(g2), max(g2))

    elif mode == 'bn_and_english-idf':
        n = 107900
        # g1 = []
        # g2 = []
        for i in indEng_dict:
            # g1.append(log10(n/len(indEng_dict[i])))
            if log10(n/len(indEng_dict[i])) < val1:
                s.write(i + '\n')
        
        for i in indBn_dict:
            # g2.append(log10(n/len(indBn_dict[i])))
            if log10(n/len(indBn_dict[i])) < val2:
                s.write(i + '\n')
        
        # print(min(g1), max(g1))
        # print(min(g2), max(g2))
    
    elif mode == 'bn_and_english-tfidf':
        n = 107900
        v = len(ind_dict)
        # g1 = []
        # g2 = []
        for i in indEng_dict:
            # g1.append(log10(n/len(indEng_dict[i])) * log10(v/indEng[i]))
            if(log10(n/len(indEng_dict[i])) * log10(v/indEng[i])) < val1:
                s.write(i + '\n')
        
        for i in indBn_dict:
            # g2.append(log10(n/len(indBn_dict[i])) * log10(v/indBn[i]))
            if (log10(n/len(indBn_dict[i])) * log10(v/indBn[i])) < val2:
                s.write(i + '\n')
        # print(min(g1), max(g1))
        # print(min(g2), max(g2))

    elif mode == 'test':
        print(len(indBn), len(indEng), len(combined_ind))
        print(Bn_words, eng_words)
    s.close()

    subprocess.call(['zip', '--delete', '/home/nitin/.pyterrier/terrier-assemblies-5.7-jar-with-dependencies.jar', 'stopword-list.txt'])
    with zipfile.ZipFile('/home/nitin/.pyterrier/terrier-assemblies-5.7-jar-with-dependencies.jar', 'a') as a:
        a.write("stopword-list.txt")

# create_stopwords(2, 0, 'test')