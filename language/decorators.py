# write a decorator using @ keyword
def decorator_function(func):
    def wrapper():
        # The purpose of the wrapper is to describe a concrete surrounding
        # logic around the function to be decorated.
        print("before the function is called")
        func()  # function to be called is available as the arg 'func' is global to wrapper
        print("after the function is called")
    return wrapper # this represents returning a function that with a concrete logic surrounding it

def say_something():
    print("this is a greeting")
# Below we show two techniques of decoration [1] and [2]

# [1] this is the clunky one :p
# Here we replace the logic of say_something function with additional logic surrounding the function call.
# We replace the keyword
say_something = decorator_function(say_something)
say_something()

# [2] This is the second technique were the say_hello keyword is replaced with the decorated counterpart
@decorator_function
def say_hello():
    print("Hello world")

say_hello()


