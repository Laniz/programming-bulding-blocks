names =[]
name = ''
counter = 0
while name != 'end':
    name = input('type the name of your friend ')
    counter += 1
    # print(name)
    # if name 
    if name != 'end':
        names.append(name)

    

# print(names)
    # for index, names in enumerate(names):
for n in names:
    print(f'your name is {n}')