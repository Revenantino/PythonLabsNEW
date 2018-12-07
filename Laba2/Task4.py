file_a = open('a.txt.txt') #bez unicoda
lines = file_a.readlines()

x = 0
count = 0
list1 = []
dictionary = {}
dictionary2 ={}

for line in lines:
    x = x + 1
    y = 0
    for word in line.split():
        y = y + 1
        word = word.lower()
        j = word[-3:]
        if j not in dictionary:

            j = word
            dictionary[j[-3:]] = []
            dictionary[j[-3:]].append("( " + j + "  line: " + str(x) + " position: " + str(y)+" )")
            dictionary2[j[-3:]] = 1

        elif j in dictionary:
            count += 1
            j = word
            dictionary[j[-3:]].append("( " + j + "  line: " + str(x) + " position: " + str(y) + " )")
            dictionary2[j[-3:]] += 1



import xml.etree.cElementTree as ET

root = ET.Element("root")
endings = ET.SubElement(root, "endings")


for i in dictionary:
        print("%s : %s" % (i, dictionary[i]))
        ET.SubElement(endings, "myword", name=str(i), quantity = str(dictionary2[i])).text = str(dictionary[i])
print (dictionary2)

tree = ET.ElementTree(root)
tree.write("c.xml", encoding = 'utf-8')