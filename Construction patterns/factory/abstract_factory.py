from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')

class Chocolate(HotDrink):
    def consume(self):
        print('This chocolate is delicious')


# Now, let's suppose that the operation of making tea or making coffee is well, both of these operations
# are so sophisticated that you need a factory to to actually sort of prepare the drink for you.



class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()

class ChocolateFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some cocoa, boil water, pour {amount}ml, enjoy!')
        return Chocolate()



class AvailableDrink(Enum): 
    COFFEE = auto()
    TEA = auto()
    CHOCOLATE = auto()

class HotDrinkMachine:
    
    initialized = False

    availaDrinks = AvailableDrink(1)

    def __init__(self):
        self.factories = []
        self.availabeDrink = AvailableDrink
  
        for d in self.availabeDrink:
            name = d.name[0] + d.name[1:].lower()
            factory_name = name + 'Factory'
            factory_instance = eval(factory_name)()
            self.factories.append((name, factory_instance))


    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()