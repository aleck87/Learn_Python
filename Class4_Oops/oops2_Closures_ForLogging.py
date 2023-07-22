# Closures : a closure is a record storing a function[a] together with an environment.
#            The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope)
#            with the value or reference to which the name was bound when the closure was created.[b] Unlike a plain function, a closure allows the function
#           to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.

import logging
logging.basicConfig(filename='example.log',level=logging.INFO)

def logger(func):
    def inner_logger(*args, **kwargs):
        logging.info('Running "{}" with argument {}'.format(func.__name__, args))
        print(func(*args))
    return inner_logger

def add(x ,y):
    return x + y

def sub(x, y):
    return x - y

add_withlogging = logger(add)
sub_withlogging = logger(sub)

add_withlogging( 5,57)
sub_withlogging( 5,57)

add_withlogging( 5,50)
sub_withlogging( 5,50)