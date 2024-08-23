def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting):
    return f'{greeting}, {name}!'

@log_decorator
def factorial(n):
    output = 1
    for num in range(2, n + 1):
        output *= num
    return output

input1 = input().strip()
input2 = input().strip()
input3 = input().strip()

a, b = map(int, input1.split())
name, greeting = input2.split()
n = int(input3)
add(a, b)
greet(name, greeting)
factorial(n)
