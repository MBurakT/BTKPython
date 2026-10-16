file = open("newfile.txt", "r", encoding = "utf-8")

# for i in file:
#     print(i, end = "")

content1 = file.read()

print("içerik 1")
print(content1)

file = open("newfile.txt", "r", encoding = "utf-8")
content2 = file.read()

print("içerik 2")
print(content2)

file.close()
