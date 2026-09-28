# a) write a function add_entry(d) that adds a new key_value pair to a dictionary d. 
#  call this function  with alist and check whether the original list changes outside the function or not




    
    
# B)  write another function reassign_dict(d) that reassigns the dictionary variable to a new variable

##  call this function  with alist and check whether the original list changes outside the function or not



def add_entry(d):
    d["new_key"] = "new_value"
    print("Inside add_entry:", d)

def reassign_dict(d):
    d = {"completely_new_key": 42}
    print("Inside reassign_dict:", d)


my_dict = {"original_key": "original_value"}
print("Before add_entry:", my_dict)
add_entry(my_dict)
print("After add_entry:", my_dict) 


print("-" * 40)

my_dict = {"original_key": "original_value"}
print("Before reassign_dict:", my_dict)
reassign_dict(my_dict)
print("After reassign_dict:", my_dict)













    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
