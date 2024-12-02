fruits = ['Apple', 'Mango', 'Kiwi']

# call first item in the list
print('Frist item in the list',fruits[0])

# call last item in the list
print('Last item of the list',fruits[-1])

# loop function
for fruit in fruits:
    print('List of fruits',fruit)

#add new item in the list
fruit = []
fruits.append('Apple')
fruits.append('Mango')
fruits.append('Kiwi')
print('New Item in the list', fruits)

# making numerical list
flag = []
for x in range(1,12):
    flag.append(x**2)
    print(flag)

# list comprehensive
flags = [x**2 for x in range (1,12)]
print('List comprehensive', flags)

#slicing a list
print('Slice', fruits[:2])

#copying a list
copy_list = fruits[:]
print('Copy list', copy_list)