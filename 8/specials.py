# mylist = [1, 2, 3]
# myString = "my String"

# print(len(mylist))
# print(len(myString))
# print(type(mylist))
# print(type(myString))


class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi oluşturuldu!")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("film silindi")


m = Movie("film adi", "yönetmen adi", 120)

print(len(m))

print(str(m))

del m
