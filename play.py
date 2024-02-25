dic = {"I" : 1 , "Love" : 2 , "You" : 3}

print(list(dic.keys())[list(dic.values()).index(2)])

h = "I am a String."

print(h.upper())

class Human:
    def __init__(self, name, age ) -> None:
        self.name = name
        self.age = age

first = Human("Esma", float(18))