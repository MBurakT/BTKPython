file = open("newfile.txt", "r", encoding = "utf-8")

content = file.read(5)

content = file.read(3)

print(content)

file.close()
