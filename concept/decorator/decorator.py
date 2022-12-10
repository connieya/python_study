def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# 일급 객체
def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 2, 3)
print(result)


# 중첩 함수
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()


# 데코레이터
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do Something before
        function()
        function()
        # Do Something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("How are you?")

# @ 를 사용하여 데코레이터 사용
say_hello()

# 데코레이터 함수 인자에 직접 전달
decorated_function = delay_decorator(say_greeting)
decorated_function()