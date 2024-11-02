# # Hello World
# a = 'Hello World!'
# print (a)

"""
>>> A more fun code - Hello World! :-))))
"""

# Importing required modules
from functools import wraps

# Metaclass that changes the behavior of a class, including a new "hello" function
class HelloMeta(type):
    def __new__(cls, name, bases, dct):
        dct['hello'] = lambda self: 'H'
        dct['world'] = lambda self: 'ello, World!'
        return super().__new__(cls, name, bases, dct)

# Decorator to transform functions of a class to always return concatenated strings
def concatenate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return ''.join(func(*args, **kwargs))
    return wrapper

# Main class, using the HelloMeta metaclass
class ComplexHello(metaclass=HelloMeta):
    def __init__(self):
        self.phrases = [self.hello, self.world]

    @concatenate
    def display(self):
        return (phrase() for phrase in self.phrases)

# Generator that generates the final result from an instance of the ComplexHello class
def generate_hello():
    instance = ComplexHello()
    yield instance.display()

# Runs "complicated" :-) code to print "Hello, World!"
if __name__ == '__main__':
    for message in generate_hello():
        print(message)
