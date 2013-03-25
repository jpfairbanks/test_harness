"""The timedict module provides decorators to wrap your functions for timing counting and logging 
as well as the timedict class to handle it using the interface of tic and toc.
"""
from time import time as time
from functools import wraps 
def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock()-t)
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, args, kwargs)
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper



class timedict(object):
    """ The global state necessary to do sophisticated timing
    acts like a key value store of times using tic and toc to start and stop the timers.

    timedict.as_dict() returns the dict from keys to the time they took. the
    keys can be any hashable type. Such as a loop iteration counter or function
    name as a string
    """

    def __init__(self, ):
        """
        Make some empty dicts
        """
        self.starts = dict()
        self.ends = dict()

    def tic(self,  key):
        """start the timer with key

        Arguments:
        - `self`: state
        - `key`: the key to access this later
        """
        self.starts[key] = time()

    def toc(self, key):
        """start the timer with key

        Arguments:
        - `self`: state
        - `key`: the key to access this later
        """
        self.ends[key] = time()-self.starts[key]

    def __str__(self):
        return self.ends.__str__()

    def as_dict(self):
        return self.ends

    def __getitem__(self, key):
        """Access the time for doing key

        :key: The task of interest using the same key as tic and toc
        :returns: The time it took

        """
        return self.ends[key]


def test():
    """Just shows of the decorators in this module
    :returns: None

    """
    @counter
    @benchmark
    @logging
    def reverse_string(string):
        return str(reversed(string))

    print(reverse_string("Able was I ere I saw Elba"))
    print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))

if __name__ == '__main__':
    test()
