def my_decorator(func):
    
    def wrapper(name):
        print("fonksiyondan önce işlemler")
        func(name)
        print("fonskiyondan sonraki işlemler")

    return wrapper

@my_decorator
def sayHello(name):
    print("Hello ", name)

sayHello("Denem")