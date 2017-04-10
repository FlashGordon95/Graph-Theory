from lxml import etree
import csv
rooms = []
hparser = etree.HTMLParser(encoding='utf-8')
tree   = etree.parse('gmit-rooms-doc.webarchive', hparser)
options = tree.xpath("//select[@name='dlObject']/option")
rooms = [option.text for option in options]
print(rooms)
out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)

