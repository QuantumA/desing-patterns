
class Person:
    def __init__(self):
        self.name = None
        self.age = None
    
    def __str__(self) -> str:
        
        return f"My name is {self.name} and my age is {self.age}"


class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.person = Person()

    def build(self):
        return self.person
        
        
    def add_field(self, type, name):
        setattr(self.person, type, name)
        return self

    def __str__(self) -> str:
        return str(self.__class__)


cb = CodeBuilder('Person') \
    .add_field('name', 'Álvaro') \
    .add_field('age', 36) \
    .build()

print(cb)
