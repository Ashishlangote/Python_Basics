class A:
    def __init__(self):
        print("In A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):
        super().__init__()  # You can access all the feature parent class
        print("In B Init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

    def feat(self):
        super().feature2()


a1 = B()
a1.feat()

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []

for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)