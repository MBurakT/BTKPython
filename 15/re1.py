import re

result = dir(re)

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

result = re.findall("Python", str)
result = len(result)

result = re.split(" ", str)

result = re.sub(" ", "-", str)

match = re.search("Python", str)

result = match.span()
result = match.start()
result = match.end()
result = match.group()
result = match.string

result = re.findall("[abc]", str)
result = re.findall("[sat]", str)
result = re.findall("[a-e]", str)
result = re.findall("[a-z]", str)
result = re.findall("[0-5]", str)
result = re.findall("[^abc]", str)
result = re.findall("[^0-9]", str)

result = re.findall("...", str)
result = re.findall("Py..on", str)

result = re.findall("^P", str)
result = re.findall("t$", str)

result = re.findall("sa*t", str)
result = re.findall("sa+t", str)
result = re.findall("sa?t", str)

result = re.findall("a{2}", str)
result = re.findall("[0-9]{2}", str)

result = re.findall("\\APython", str)
result = re.findall("saat\\Z", str)

print(result)
