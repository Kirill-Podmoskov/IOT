class C:
    pass
instance = C()

print(type(instance))
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} сидит.")

    def roll_over(self):
        print(f"{self.name} перекатывается.")

my_dog = Dog('willie', 6)

print(f"Имя: {my_dog.name}, Возраст: {my_dog.age}")

my_dog.sit()
my_dog.roll_over()

another_dog = Dog('lucy', 3)

print(f"Имя: {another_dog.name}, Возраст: {another_dog.age}")

another_dog.sit()
another_dog.roll_over()

class Human:
    default_name = "Default Name"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        house_info = "Нет жилья" if not self.__house else f"Дом: {self.__house._area} м² за {self.__house._price} ед."
        print(f"Имя: {self.name}, Возраст: {self.age}, Деньги: {self.__money}, {house_info}")
    @staticmethod
    def default_info():
        print(f"Имя по умолчанию: {Human.default_name}, Возраст по умолчанию: {Human.default_age}")
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
    def earn_money(self, amount):
        self.__money += amount
        print(f"{self.name} заработал(а) {amount}. Баланс: {self.__money}")
    def buy_house(self, house, discount=0):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
            print(f"{self.name} купил(а) дом площадью {house._area} м² за {final_price} ед.")
        else:
            print(f"{self.name} не хватает денег для покупки дома. Требуется {final_price}, доступно {self.__money}.")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)
class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)

#Тесты

Human.default_info()#1
person = Human("Иван", 35)#2
person.info()#3
small_house = SmallHouse(50000)#4
person.buy_house(small_house)#5
person.earn_money(60000)#6
person.buy_house(small_house)#7
person.info()#8
