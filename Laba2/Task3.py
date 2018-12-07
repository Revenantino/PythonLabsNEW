import xml.etree.ElementTree as ET
from collections import defaultdict
d = defaultdict(int)
wordcount = []
list1 = []
for word in open('a.txt.txt', encoding='utf-8').read().split():
    d[word] += 1
    wordcount.append(word)
print(d)
data = ET.Element('data')
words_xml = ET.SubElement(data,'wordcount')

for i in d.keys():
    ET.SubElement(words_xml, 'word', name=i).text = 'count = ' + str(d[i])
mydata = ET.ElementTree(data)
myfile = open("c.xml", "w")
mydata.write("c.xml", encoding="utf-8")
myfile.close()