class KgToPounds:
    def __init__(self, kg):
        self.kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError("Килограммы задаются только числами")

weight = KgToPounds(12)

print(weight.to_pounds())

print(weight.kg)

weight.kg = 41
print(weight.kg)


try:
    weight.kg = "десять"
except ValueError as e:
    print(e)

