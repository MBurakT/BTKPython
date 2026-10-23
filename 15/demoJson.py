import json
import os

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUsers = None

        # load users from .json file
        self.loadUsers()

    
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding = "utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(user["username"], user["password"], user["email"])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanıcı oluşturuldu.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username:
                if user.password == password:
                    self.isLoggedIn = True
                    self.currentUsers = user
                    print("Login işlemi yapıldı.")
                    break

        if not self.isLoggedIn:
            print("Kullanıcı adı veya parola yanlış!")

    def logout(self):
        self.isLoggedIn = False
        self.currentUsers = None
        print("Logout işlemi yapıldı.")

    def identity(self):
        if self.isLoggedIn:
            print(f"{self.currentUsers.username}")

    def savetoFile(self):

        liste = []

        for user in self.users:
            liste.append(json.dumps(user.__dict__))

        with open("users.json", "w") as file:
            json.dump(liste, file)

repository = UserRepository()

while True:
    print("Menü".center(50, "*"))
    
    secim = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nSeçiminiz: ")
    
    if secim == "5":
        break

    if secim == "1":
        username = input("username: ")
        password = input("password: ")
        email = input("email: ")

        user = User(username, password, email)
        repository.register(user)

        print(repository.users)

    elif secim == "2":
        username = input("username: ")
        password = input("password: ")

        repository.login(username, password)

    elif secim == "3":
        repository.logout()

    elif secim == "4":
        repository.identity()

    else:
        print("Girdiğiniz seçim mevcut değil! Lütfen tekrar deneyiniz.")
