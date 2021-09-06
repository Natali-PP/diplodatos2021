import re

with open('./Victorian-Place-Names-and-Councils.txt') as fin, open('victoria-councils-transformed.txt', 'w') as fout:
    for line in fin:
        #line.replace('\t', ',')
        fout.write(re.sub(r'[(]\d{4}[)]','',line))

#with open('./Victorian-Place-Names-and-Councils.txt') as fin, open('victoria-councils-transformed', 'w') as fout:
#    for line in fin:
#        #line.replace('\t', ',')
#        fout.write(re.sub(r'[(]\d{4}[)]','',line))
