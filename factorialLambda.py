def recursive_lambda(func):
    def ret(*args):
        return func(ret, *args)
    return ret

number=int(input())
print(recursive_lambda(lambda factorial, x: x * factorial(x - 1) if x > 1 else 1)(number))