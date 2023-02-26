import re

#with open('data.txt', 'r') as f:
 #   data = f.read()
  #  print(data)

file = open('data_language_tagged_combined.txt', 'r', encoding="utf8")
lines = file.readlines()
count = 1

for line in lines:
    # output = open('dataset/baseline/corpus_baseline/%d.txt' % count, 'w', encoding="utf8")
    output = open('dataset/tagged/tagged_corpus.trec', 'a', encoding="utf8")
    output.write('<DOC>\n')
    output.write('<DOCNO>%d</DOCNO>\n' %count)
    output.write('<HEAD> </HEAD>\n')
    output.write('<BODY>\n')
    s = ''.join(line.strip())
    s = re.sub(' +', ' ', re.sub(r'[^\x00-\x7F]+', ' ', s))
    output.write(s)
    output.write('\n')
    output.write('</BODY>\n')
    output.write('</DOC>\n')
    output.close()
    print("Line : {}".format(line.strip()))
    count+=1
