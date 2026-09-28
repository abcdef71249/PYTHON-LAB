#  decorater called show_info that prints
# calling function before the function runs
#  functon exceuted after the function ends
#  apply it to a function square(num) that returns the square of a number


def show_info(func):
    def wrapper(num):
        print(f"Calling function {func.__name__}  {num}")
        result = func(num)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper


@show_info
def square(num):
    return num ** 2


num = int(input("Enter a number: "))
square(num)


