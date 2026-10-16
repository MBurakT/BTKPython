file = open("newfile.txt", "r", encoding = "utf-8")

liste = file.readlines()

print(liste)

file.close()
