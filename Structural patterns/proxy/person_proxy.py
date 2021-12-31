class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'

class ResponsiblePerson:
    def __init__(self, person):
        self.person = person
    
    @property
    def age(self):
        return self.person.age


    def drink(self):
        if self.person.age < 18:
            return "too young"
            
        self.person.drink()

    def drive(self):
        if self.person.age < 1:
            return "too young"
            
        self.person.drive()

    def drink_and_drive(self):
        return "dead"


