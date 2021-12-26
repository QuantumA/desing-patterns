"""you are given a class called Person. 
The person has two attributes: id, and name.
Please implement a PersonFactory that has a non-static create_person() method
that takes a person's name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created.
So, the first person the factory makes should have Id=0, second Id=1 and so on.
"""

from itertools import count

class Person:
    
    _ids = count(0)

    def __init__(self, name):
        self.name = name
        self.id = next(self._ids)

class PersonFactory:
    def create_person(self, name):
        return Person(name)



if __name__=="__main__":
    pf = PersonFactory()

    p1 = pf.create_person('Chris')

    assert p1.name == 'Chris'
    assert p1.id == 0

    p2 = pf.create_person('Sarah')
    assert p2.name == 'Sarah'
    assert p2.id == 1
