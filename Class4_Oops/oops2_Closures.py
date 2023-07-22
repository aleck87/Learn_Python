# Closures : a closure is a record storing a function[a] together with an environment.
#            The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope)
#            with the value or reference to which the name was bound when the closure was created.[b] Unlike a plain function, a closure allows the function
#           to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope.

def outer_func():
    msg = "Hi"

    def inner_func():
        print(msg)

    return inner_func

# now the local/Free  variable msg has been captured in the variable my_func along with the call of outer_func !!!
# so the whole env has been assigned to my_func
my_func = outer_func()
my_func()

def outer_func1(msg):

    def inner_func():
        print(msg)

    return inner_func

hi_func = outer_func1('hi')
hello_func = outer_func1('hello')

hi_func()
hello_func()