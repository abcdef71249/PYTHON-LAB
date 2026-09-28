#  genrator  funtion countdown(n) that yields numbers from n to 0 
#  use a loop to print the numbers taking user input for the number

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


num = int(input("Enter a number: "))
for number in countdown(num):
    print(number)
