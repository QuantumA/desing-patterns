"""Our system has any number of instances of Participant classes.
Each Participant has a value integer attribute, initially zero.
A participant can say() a particular value, which is broadcast to all other participants.
At this point in time, every other participant is obliged
to increase their value by the value being broadcast."""


class Participant:
    def __init__(self, mediator, name):
        self.name = name
        self.value = 0
        self.mediator = mediator
        self.mediator.join(self)

    def say(self, value):
        self.mediator.broadcast(self, value)
        
    def increase(self, value):
        self.value += value
        print(f"{self.name} now have value = {self.value}")
        


class MediatorRoom:
    def __init__(self) -> None:
        self.participants = []

    def broadcast(self, who: Participant, value: int):
        print(f"{who.name} broadcasts the value {value}")
        for p in self.participants:
            if p != who:
                p.increase(value)

    def join(self, participant):
        self.participants.append(participant)


if __name__ == '__main__':
    
    mediatorRoom = MediatorRoom()

    p1 = Participant(mediator=mediatorRoom, name="Participant 1")
    p2 = Participant(mediator=mediatorRoom, name="Participant 2")
    p3 = Participant(mediator=mediatorRoom, name="Participant 3")
    p4 = Participant(mediator=mediatorRoom, name="Participant 4")

    p1.say(3)

    p3.say(2)
