import os

result = dir(os)

result = os.name
result = os.getcwd()
print(result)

# os.mkdir("newdirectory")

os.chdir("C:\\")
result = os.getcwd()

print(result)

result = os.listdir()

print(result)

for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)

