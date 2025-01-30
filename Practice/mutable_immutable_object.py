# Mutable Objects: can be modified after creation; Lists, sets & Dictionaries
# Immutable Objects: cannot be modified after creation; Tuple, Strings and Numbers

# Example 
num = 32
text = "Hello"
my_tuple = (1,2,3)

# trying to modify will raise an error 
try:
    num += 10
    # text[0] = 'M' # This will raise a TypeError
    # my_tuple[0] = 100 #This will raise a TypeError
except TypeError as e:
    print(f"Error: {e}")


# Mutual Objects
my_list = [1,2,3]
my_dict = {'a': 1, 'b':2}

# Can be modified without issues
my_list.append(5)
print(my_list)
del my_dict['a']
print(my_dict)