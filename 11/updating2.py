with open("newfile.txt", "a", encoding = "utf-8") as file:
    file.write("\nEmel Turan")

with open("newfile.txt", "r", encoding = "utf-8") as file:
    content = file.read()
    print(content)