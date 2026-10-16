with open("newfile.txt", "r+", encoding = "utf-8") as file:
    file.seek(20)
    file.write("Denem")
    
with open("newfile.txt", "r+", encoding = "utf-8") as file:
    print(file.read())

