html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>
    <h1 id="header">Python Kursu</h1>

    <div class="grup1">
        <h2>Programlama</h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>Modüller</h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">
    
</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
title = soup.title
head = soup.head
body = soup.body
titleName = title.name
titleString = title.string

h1 = soup.h1
h2 = soup.h2
h2Name = h2.name
h2String = h2.string
findAllH2 = soup.find_all("h2")

div = soup.div
findAllDiv = soup.find_all("div")


print(result)
print(title)
print(head)
print(body)
print(titleName)
print()

print(h1)
print(h2)
print(h2Name)
print(h2String)
print(findAllH2)
print()

print(div)
print(findAllDiv)
print()