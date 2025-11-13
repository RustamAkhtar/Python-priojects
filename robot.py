class robot:
    age = 11
    name = "Robby the Robot"

    def introduction(self):
        print("Hi I am a helpful robot!")

    def details(self):
        print("My name is", self.name)
        print("My age is", self.age)

ob = robot()

ob.introduction()
ob.details()