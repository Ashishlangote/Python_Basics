from abc import ABC, abstractmethod


class Implement(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass


class Word(Implement):
    def open(self):
        print("Open")

    def fun():
        print("Close")

    def save(self):
        print("Save")


class Excel(Word):
    def save(self):
        print("Save")


w1 = Word()
e1 = Excel()
w1.open()
w1.save()
e1.open()
e1.save()


# class Bank:
#     interest_rate = 0.03

#     def __init__(self, amt):
#         self.balance = amt

#     @classmethod
#     def calculate_interest(cls, amt):
#         return amt * cls.interest_rate

#     @staticmethod
#     def offers(ir):
#         print(f"Available balance {ir} years FD @ {ir * 2} p.a")


# p1 = Bank(10000)
# p1.interest_rate
# Bank.interest_rate

# p1.balance += p1.calculate_interest(p1.balance)
# print(p1.balance)
# p1.offers(5)
