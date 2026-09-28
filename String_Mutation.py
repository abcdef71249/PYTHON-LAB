# write a function change_string(s) that tries to replace the first character of the string with the " x"
#  call this function  with alist and check whether the original list changes outside the function or not


def change_string(s):
    if s: # check if the string is not empty
        s = "x" + s[1:] # create a new string with 'x' as the first character
        
    return s




original_string = "hello"
print("Original string:", original_string)
new_string = change_string(original_string) # calling this function with original_string
print("New string:", new_string)


# using anyothr method to change the string
def change_string_alternative(s):
    if s: # check if the string is not empty
        s = s.replace(s[0], "x", 1) # replace the first character with 'x'
        
    return s

new_string_alternative = change_string_alternative(original_string)
print("New string (alternative method):", new_string_alternative)