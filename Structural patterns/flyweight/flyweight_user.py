import random
import string
import sys


class UserFlyWeight:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1
        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])



if __name__=="__main__":
    # users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    # for first in first_names:
    #     for last in last_names:
    #         users.append(UserFlyWeight(f'{first} {last}'))
            
    
    # [print(str(user)) for user in users]
    # print(len(users))
    
    u2 = UserFlyWeight('Jim Jones')
    u3 = UserFlyWeight('Frank Jones')
    print(u2.names)
    print(u3.names)
    print(UserFlyWeight.strings)


    users2 = []

    for first in first_names:
        for last in last_names:
            users2.append(UserFlyWeight(f'{first} {last}'))

    print(UserFlyWeight.strings)
    print(len(UserFlyWeight.strings))

    