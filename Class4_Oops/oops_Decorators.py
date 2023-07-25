def decorator_func(orig_func):
    def wrapper_func(*args, **kwargs):
        print('wrapper function executed before {}'.format(orig_func.__name__))
        return orig_func(*args, **kwargs)
    return wrapper_func

#1 So far we need to call decorated_func with an variable keeping the closure for it but when we use
# the name of decorator_func as @decorated_func above the function display, it has the functionality of wrapper_func added automatically
# this way decorated_func automatically and so we can modify the functionality of the wrapper_func without touching the original display function
@decorator_func # this means display = decorator_func(display)
def display():
    print('Display function ran')

@decorator_func
def display_info(name, age):
    print('display_info function ran with arguments: {}, {}'.format(name, age))

#1 decorated_display = decorator_func(display)
#1 decorated_display()

display()

display_info('John', 35)
