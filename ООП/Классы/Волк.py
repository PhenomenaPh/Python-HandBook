class Programmer:
    def __init__(self, name, position) -> None:
        self.name = name
        self.position = position
        self.money = 0
        self.hours = 0

        if self.position == "Junior":
            self.wage = 10
        elif self.position == "Middle":
            self.wage = 15
        elif self.position == "Senior":
            self.wage = 20

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
            self.wage = 15
        elif self.position == "Middle":
            self.position = "Senior"
            self.wage = 20
        elif self.position == "Senior":
            self.wage += 1

    def work(self, time):
        self.money += time * self.wage
        self.hours += time

    def info(self):
        return f"{self.name} {self.hours}ч. {self.money}тгр."


programmer = Programmer("Васильев Иван", "Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
