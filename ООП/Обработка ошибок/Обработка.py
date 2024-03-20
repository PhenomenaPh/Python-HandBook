def func(x):
    return x


try:
    func(2)
except TypeError as tp:
    print(type(tp).__name__)
except ValueError as v:
    print(type(v).__name__)
except SystemError as se:
    print(type(se).__name__)
else:
    print("No Exceptions")
