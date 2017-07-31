import xml.dom.minidom
from datetime import datetime

# inputStr = str(raw_input('Date (yyyy, mm, dd):'))
# try:
#     inputDate = datetime.strptime(inputStr, "%Y, %m, %d")
# except ValueError:
#     print "Incorrect Date"
#     exit(0)

#print inputDate

# use the parse() function to load and parse an XML file
doc = xml.dom.minidom.parse("BookData1.xml")


# print out the document node and the name of the first child tag
for book in doc.getElementsByTagName('book'):
    book_id = book.getAttributeNode('id').nodeValue
    book_title = book.getElementsByTagName('title')[0].firstChild.nodeValue
    book_date = book.getElementsByTagName('publish_date')[0].firstChild.nodeValue
    book_price = book.getElementsByTagName('price')[0].firstChild
    book_price.data = float(book_price.data) * 1.2


    # book_price = book.getElementsByTagName('price')[0].firstChild
    # book_price.data = unicode(float(book_price.data) * 1.2)




    publishDate = datetime.strptime(book_date, "%Y-%m-%d")

    print ('********Book Details*********')
    print ('Book Id:', book_id)
    print ('Book Title:', book_title)
    print ('Book Publish_date:', book_date)
    print ('Book price:', book_price.nodeValue)

xmlFile = open("BookData1.xml", "w")
doc.writexml(xmlFile)
xmlFile.close()

myString = "This is a sample string, it contains comma,"
newString = myString.replace(",",".")
print "New string is " + newString