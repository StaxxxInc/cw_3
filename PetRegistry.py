class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

    def __enter__(self):
        self.counter = Counter()  # Create a new Counter object
        return self.counter

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            raise Exception("Ошибка при работе с объектом Counter.")
        self.counter = None
    
    def __repr__(self):
        return f"Имя = {self.name}, Порода = {self.animal_type}"

class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

def main():
    animals = []

    while True:
        print("1. Принять нового питомца")
        print("2. Поместить питомца в правильный класс")
        print("3. Посмотреть список команд для питомца")
        print("4. Научить питомца новым командам")
        print("5. Вывесьти список всех питомцев")
        print("6. Выход")

        choice = input("Введите свой выбор: ")

        if choice == "1":
            name = input("Введите имя питомца: ")
            animal_type = input("Введите породу питомца: ")
            animals.append(Animal(name, animal_type))
            with animals[-1] as counter:  # Creating a new animal increments the Counter value
                counter.add()
                print("Питомец успешно добавлен!")

        elif choice == "2":
            name = input("Введите имя: ")
            animal_type = input("Введите породу питомца: ")

            animal = None
            for a in animals:
                if a.name == name and a.animal_type == animal_type:
                    animal = a

            if animal is not None:
                print("Питомец найден: ", animal.name)
                class_name = type(animal).__name__
                print("Класс питомца: ", class_name)
            else:
                print("Питомец не найден!")

        elif choice == "3":
            name = input("Введите имя: ")
            animal_type = input("Введите породу: ")

            animal = None
            for a in animals:
                if a.name == name and a.animal_type == animal_type:
                    animal = a

            if animal is not None:
                print("Команды для", animal.name, ": ", animal.get_commands())
            else:
                print("Питомец не найден!")

        elif choice == "4":
            name = input("Введите имя:")
            animal_type = input("Введите породу: ")

            animal = None
            for a in animals:
                if a.name == name and a.animal_type == animal_type:
                    animal = a

            if animal is not None:
                command = input("Введите новую команду: ")
                animal.add_command(command)
                print("Команда успешно добавлена!")
            else:
                print("Питомец не найден")

        elif choice == "5":
            print("Вывести список всех питомцев:")
            for animal in animals:
                print(animal)

        elif choice == "6":
            break

if __name__ == "__main__":
    main()


#  класс Counter создается с помощью метода add(), который увеличивает значение 
#  внутренней переменной count на 1. Counter используется в классе Animal 
#  в качестве менеджера контекста с использованием методов __enter__ и __exit__. 
#  Это позволяет программе автоматически создавать новый объект Counter при входе 
#  в блок with и правильно обрабатывать любые исключения, которые могут возникнуть 
#  при работе с объектом Counter. Если в блоке with возникает исключение, будет 
#  вызван метод __exit__ и возникнет исключение.
