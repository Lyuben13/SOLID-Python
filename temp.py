class User:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    # Свойство за достъп до възрастта
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0 or age > 130:
            raise ValueError("Age must be between 0 and 130")
        self._age = age

    # Метод за показване на информацията за потребителя
    def display(self):
        print(f"{self.name} {self.last_name}, Age: {self.age}")

    # Метод за въвеждане на информация за потребителя
    def input(self):
        self.name = input("Input name: ")
        self.last_name = input("Input last name: ")
        self.age = int(input("Input age: "))


# Създаване на обект от клас User, показване на информацията,
# актуализиране с въведените данни от потребителя и повторно показване.
obj = User("Bill", "Windows", 34)
obj.display()
obj.input()
obj.display()
