from lxml import etree
import csv
'''
  Steps:
  1. Initialise empty array for our result
  2. Get the HTML page into the parser and receive the DOM Tree
  3. Receive the Select element the holds all the room data, located by the xpath
  4. Iterate over the object and strip it out for the objects text only (Before we do this each index is actually a HTML element.)
  5. Open a csv writer
  6. Iterate over the room array again this time adding it to a row in the CSV with a index.
  7. ????
  8. Profit.
    
'''
rooms = []  #Initialise an empty array
hparser = etree.HTMLParser(encoding='utf-8') #Prepare the HTMLParser and set the encoding (Important, gmit website uses latin1 encoding)
tree   = etree.parse('gmit-rooms-doc.webarchive', hparser) #Get the DOM tree from the previous parser
options = tree.xpath("//select[@name='dlObject']/option") #Get all the rooms in the 'select' HTML element. This will be turned into an array of <options> elements
rooms = [option.text for option in options] # Because we dont want the HTML stuff, only the text, we use a for in loop to get the element and reassign it to only the text of the element.
print(rooms) #Finally print the rooms to screen.
out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)

i=0
row = [rooms,1]
for room in rooms:
    row = [room, i]
    out.writerow(row)
    i += 1
