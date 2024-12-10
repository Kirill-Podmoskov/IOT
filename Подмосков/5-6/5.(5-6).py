class Nikola:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.age = age
        if name == "Николай":
            self.name = name
        else:
            self.name = f"Я не {name}, а Николай"

person1 = Nikola('Иван', 31)
person2 = Nikola('Николай', 14)

print(person1.name)
print(person2.name)

try:
    person2.surname = 'Петров'
except AttributeError as e:
    print(e)