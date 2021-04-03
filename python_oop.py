# parent class
class Animal:
    
    def __init__(self):
        print("Provide animal name")

    def whoisThis(self):
        print("animal")

    def swim(self):
        print("Run faster")

# child class
class Lion(Animal):

    def __init__(self):
        # call super() function
        super().__init__()
        print("lion is ready")

    
    def whoisThis(self):
        print("Lion")

    def run(self):
        print("Lion Run faster")

lion = Lion()
lion.whoisThis()
lion.run()
