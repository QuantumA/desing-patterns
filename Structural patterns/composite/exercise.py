""" Consider the code presented below. We have two classes called SingleValue and ManyValues. 
SingleValue stores just one numeric value, but ManyValues can store either numeric values or SingleValue objects. 

You are asked to give both SingleValue and ManyValues a property member called sum that returns a sum of all the values that the object contains. 
Please ensure that there is only a single method that realizes the property sum, not multiple methods.

"""


from abc import ABC
from collections.abc import Iterable

class Sumable(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for v in self:
            for c in v:
                result += c
                
        return result
            

class SingleValue(Sumable):
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        yield self.value

class ManyValues(list, Sumable):

    pass


