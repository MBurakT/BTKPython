def my_decorator(func):
    
    def wrapper():
        print("fonksiyondan önce işlemler")
        func()
        print("fonskiyondan sonraki işlemler")

    return wrapper

def sayHello():
    print("Hello")

def sayGreeting():
    print("Greeting")

sayHello = my_decorator(sayHello)
sayGreeting = my_decorator(sayGreeting)

sayHello()
sayGreeting()
