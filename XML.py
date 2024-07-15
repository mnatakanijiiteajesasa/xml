books.xml
<library>
 <book>
    <title>Python Programming</title>
    <author>John Doe </title>
    <price>29.9</price>
 </book>


import xml.etree.ElementTree as ET
tree = ET.parse("books.xml")
root = tree.getroot()

for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    price = book.find("price").text
    print("Title:", title)
    print("author:", author)
    print("price:", price)
    print()






