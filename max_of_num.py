# 4. write a function to find the max of two numbers taking input from the user
def find_max():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return max(num1, num2) # using the inuilt max() function to find the maximum of the two numbers


print("The maximum of the two numbers is:", find_max()) # calling the function and print the result




# now withput using the inbuilt max() function

def find_max_without_max():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 > num2:
        return num1
    else:
        return num2
    
    
print("The maximum of the two numbers is:", find_max_without_max()) # calling the function