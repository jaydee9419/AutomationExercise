import random
import string


def randomMail(size=5, chars=string.ascii_lowercase):
    return "".join(random.choice(chars) for x in range(size))


def randomName(size=5, chars=string.ascii_lowercase):
    return "".join(random.choice(chars) for x in range(size))
