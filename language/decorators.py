# I used this article as reference on pyton deecorators
# https://realpython.com/primer-on-python-decorators/#decorating-functions-with-arguments

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
# say_something = decorator_function(say_something)
# say_something()

# [2] This is the second technique were the say_hello keyword is replaced with the decorated counterpart
@decorator_function
def say_hello():
    print("Hello world")

# say_hello()


'''
Decoration of functions with arguments
----------
The primer describes the following way to create a decorator
for functions with arguments.
'''
def decorator_for_arged_function(func):
    def wrapper(*args, **kwargs):
        print('before the function is called')
        func(*args, **kwargs)
        print('after the function is called')
    return wrapper

@decorator_for_arged_function
def say_hello_to(name):
    print("Hello {0}. I hope you are doing well.".format(name))


# say_hello_to("Bhalchandra")

'''
In this case we can also enforce particular arguments in wrapper
and freeze the function arguments that can be specified. Below we dicuss
an example. 

*args would allow any arbitrary arguments to be passed to the wrapped functions
'''
def decorator_for_arged_function_specific(func):
    def wrapper(name):
        print(decorator_for_arged_function_specific)
        print('before the function is called')
        func(name)
        print('after the function is called')
    return wrapper

@decorator_for_arged_function_specific
def say_hello_to(name):
    print("Hello {0}. I hope you are doing well.".format(name))


# say_hello_to("Bhalchandra")


'''
Try with functools
Why we use functools.wrap is to preserve the name / help information about
the functions being wrapped.
'''
import functools

def decorator_with_functools(func):
    @functools.wraps(func)
    def wrapper(name):
        print('before the function decorator_with_functools is called')
        func(name)
        print('after the function decorator_with_functools is called')
    return wrapper

@decorator_with_functools
def say_hello_to(name):
    print("Hello {0}. I hope you are doing well.".format(name))


# say_hello_to("Bhalchandra")

'''
Try making a decorator that returns the runtime and also returns the result
'''
def track_run_time(func):
    # we don't know yet what arguments this wrapper will be taking
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # this way the decorator can be applied to any function
        import time
        start_time = time.time()
        return_value = func(*args, **kwargs)
        end_time = time.time()
        print("This programme took {0} seconds to run.".format(end_time - start_time))
        return return_value
    return wrapper

@track_run_time
def quicksort_non_recur(array):
    return quicksort(array, 0, len(array) - 1)

def quicksort(array, low, high):
    if low < high:
        array, pdx = partition(array, low, high)
        array = quicksort(array, low, pdx-1)
        array = quicksort(array, pdx+1, high)
    return array
        
def partition(array, low, high):
    pdx = high
    pivot = array[pdx]
    i = low
    for j in range(low, high+1):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i = i+1
    return array, i-1


import numpy as np
arr = np.arange(1000000)
np.random.shuffle(arr)

quicksort_non_recur(arr)




        



