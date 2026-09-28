#  create a decorater that doubles the result of a function
#  apply it to to a functio(a,b) that returns the sum of two numbers


def double_result(func):
    def wrapper(a, b):
        result = func(a, b)
        doubled_result = result * 2
        return doubled_result
    return wrapper


@double_result
def add(a, b):
    return a + b


doubled_sum = add(3, 4)
print("Doubled sum:", doubled_sum)


