# Public
# class BankAccount:

#     def __init__(self, name, bal):
#         self.name = name
#         self.bal = bal

#     def deposit(self, amt):
#         self.bal += amt
#         return self.bal

#     def withdraw(self, amt):
#         self.bal -= amt
#         return self.bal


# p1 = BankAccount("Ashish", 2000)
# p1.deposit(500)
# print(p1.name, p1.bal)


# Encapsulation Access specifiers 1.Public 2.Private 3.Protected
# Private

class BankAccount:

    def __init__(self, name, bal):
        self.__name = name
        self.__bal = bal

    # Getter and Setter method

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def bal(self):
        return self.__bal

    @bal.setter
    def bal(self, new_bal):
        self.__bal = new_bal

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def __deposit(self, amt):
        self.__bal += amt
        return self.__bal

    def __withdraw(self, amt):
        self.__bal -= amt
        return self.__bal


p1 = BankAccount("Ashish", 2000)
# p1.set_name("Raju")
# print(p1.get_name())
p1.bal = 3000
p1._BankAccount__withdraw(200)
print(p1.bal)
