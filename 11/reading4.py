file = open("newfile.txt", "r", encoding = "utf-8")

print(file.readline(), end = "")
print(file.readline(), end = "")
print(file.readline(), end = "")
print(file.readline(), end = "")

file.close()
