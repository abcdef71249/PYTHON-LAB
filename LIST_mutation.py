# write a function remove_last(lst) that removes the last element of a list
#  call this function  with alist and check whether the original list changes outside the function or not

def remove_last(lst):
    if lst: # check if the list is not empty
        lst.pop() # pop() removes the last element from the list
        
    return lst

alist = [1, 2, 3, 4, 5]
print("Original list:", alist)
remove_last(alist) #   calling this function with alist
print("List after removing last element:", alist)