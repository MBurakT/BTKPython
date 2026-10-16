try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x / y)
    
except (ZeroDivisionError, ValueError) as e:
    print("yanlış bilgi girdiniz!")
    print(e)   
