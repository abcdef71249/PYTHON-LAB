#   generators even numbers (limit) that  yeilds all even numbers up to the given limit 
#  use to print all numbers up to 10 user input taken 


def even_numbers(limit):
	for number in range(0, limit + 1, 2):
		yield number

limit = int(input("Enter the limit: "))
for number in even_numbers(limit):
	print(number)
    


