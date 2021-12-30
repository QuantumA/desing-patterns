import random
import string
import sys

class User:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f'My name is {self.name}'

def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])


if __name__ == '__main__':
    users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))
            
    
    [print(str(user)) for user in users]
    print(len(users))
    
    
    
