# 1. list of 5 fruits ,print 2nd and 4th itm and replace the last with mango and print the list
fruits = [ "apple", "banana", "cherry", "date", "strawberry"]
print("2nd fruit:", fruits[1])
print("4th fruit:", fruits[3])
fruits[4] = "mango"
print("Updated list:", fruits)



# 2.take 10 integers from user and store it in list then find sum and avg without summ()
numbers = []
for _ in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)
print("Numbers entered:", numbers)  
    
total_sum = 0 # initlaize sum variable as zero
for number in numbers:
    total_sum += number
average = total_sum / len(numbers) 
print("Sum:", total_sum)
print("Average:", average)



#3.take 7 integers from user and store it in list then find max and min without using max() and min()
numbers = []
for _ in range(7):
    num = int(input("Enter an integer: "))
    numbers.append(num)
print("Numbers entered:", numbers) 

max_num = numbers[0]
min_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print("Maximum:", max_num)
print("Minimum:", min_num)


#4. input integers into a list  WITHPOUT SPACES and remove dupliactes while preserving the order of elements
numbers = input("Enter integers without spaces: ")
unique_numbers = []
for char in numbers:
    if char not in unique_numbers:
        unique_numbers.append(char)
print("Unique integers:", unique_numbers)
    



#5. Input a list of strings FROM USER and reverse it without using reverse and slicing
a = []
n = int(input("Enter the number of strings: "))
for _ in range(n):
    string = input("Enter a string: ")
    a.append(string)

reversed_list = []
for i in range(len(a) - 1, -1, -1):
    reversed_list.append(a[i])
print("Reversed list:", reversed_list)

