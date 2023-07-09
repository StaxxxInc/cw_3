class Animal:
    def __init__(self, name, command, date_of_birth):
        self.name = name
        self.command = command
        self.date_of_birth = date_of_birth

    def execute_command(self):
        print(f"{self.name} выполнение команды: {self.command}")

class HomeAnimal(Animal):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)

class BeastOfBurden(Animal):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)

class Dog(HomeAnimal):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)

class Cat(HomeAnimal):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)

class Hamster(HomeAnimal):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)

class Horse(BeastOfBurden):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)

class Camel(BeastOfBurden):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)

class Donkey(BeastOfBurden):
    def __init__(self, name, command, date_of_birth):
        super().__init__(name, command, date_of_birth)
