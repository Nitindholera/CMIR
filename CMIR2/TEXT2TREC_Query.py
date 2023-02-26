import re

#with open('input.txt', 'r') as f:
 #   data = f.read()
  #  print(data)

file = open('query.txt', 'r', encoding="utf8")
lines = file.readlines()
count = 1


output = open('baseline_query.trec', 'w', encoding="utf8")
output.write('<topics>\n')
for line in lines:   
    s = ''.join(line.strip())
    s = re.sub(' +', ' ', re.sub(r'[^\x00-\x7F]+', ' ', s))
    output.write('<top>\n')
    output.write('<num>%d</num>\n' %count)
    output.write('<title>\n')
    output.write(s)
    output.write('</title>\n')
    output.write('<desc>\n')
    output.write(s)
    output.write('</desc>\n')
    output.write('<narr>\n')
    output.write(s)
    output.write('\n')
    output.write('</narr>\n')
    output.write('</top>\n')
    # print("Line : {}".format(line.strip()))
    print(count)
    count+=1
output.write('</topics>')
output.close()