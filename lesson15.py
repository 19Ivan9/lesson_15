from functools import wraps
#TACK1
def logger(func):
    @wraps(func)
    def wrap(*args):
        return func(*args)
    return wrap

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

x = add(6, 6)
y = square_all(6, 6,5,2,1,4,3)
print(x)
print(y)

#TACK2

def stop_words(words: list):
    def function(func):
        def wrapper(*args):
            fun = func(*args)
            for stop in words:
                fun = fun.replace(stop,'*')
            return fun
        return wrapper
    return function

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan('Steve'))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

#TACK3

def arg_rules(type_: type, max_length: int, contains: list):
    def rules(func):
        def wrapper(name):
            fun = func(name)
            if type(name) != type_:
                print('Error: invalid type!')
                return False
            if len(name) > max_length:
                print('Error: invalid size')
                return False
            for contain in contains:
                if name.find(contain) == -1:
                    print('Error: not found')
                    return False
            return fun
        return wrapper
    return rules

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

p = create_slogan('johndoe05@gmail.com')
t = create_slogan('S@SH05')
print(p)
print(t)

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'