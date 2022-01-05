"""Our system has any number of instances of Participant classes.
Each Participant has a value integer attribute, initially zero.
A participant can say() a particular value, which is broadcast to all other participants.
At this point in time, every other participant is obliged
to increase their value by the value being broadcast."""



from typing import Any

class Participant:

    instances = 0

    def __init__(self, mediator) -> None:
        self.__class__.instances += 1
        self.name = f'Participant {self.instances}'
        self.value = 0
        self.mediator = mediator
        mediator.alert.append(self.mediator_alert)
    
    def say(self, value):
        self.mediator.broadcast(self, value)

    def mediator_alert(self, sender, value):
        if sender!= self:
            self.value += value

        print(f'{self.name} has now a value = {self.value}')


class Event(list):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        for item in self:
            item(*args, **kwargs)

class Mediator:
    def __init__(self):
        self.alert = Event()

    def broadcast(self, sender, value):
        print(f"{sender.name} broadcasts the value {value}")
        self.alert(sender, value)


if __name__ == '__main__':
    
    mediatorRoom = Mediator()

    p1 = Participant(mediator=mediatorRoom)
    p2 = Participant(mediator=mediatorRoom)
    p3 = Participant(mediator=mediatorRoom)
    p4 = Participant(mediator=mediatorRoom)

    p1.say(3)
    p3.say(2)


    p5 = Participant(mediator=mediatorRoom)
    p6 = Participant(mediator=mediatorRoom)
    p7 = Participant(mediator=mediatorRoom)
    p8 = Participant(mediator=mediatorRoom)

    p8.say(8)
    p3.say(1)
