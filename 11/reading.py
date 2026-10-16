try:
    file = open("newfile.txt", "r")
    print(file)

except FileNotFoundError:
    print("Dosya okuma hatası!")

finally:
    file.close()
    print("dosya kapandı.")