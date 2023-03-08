fruits = ['apple', 'banana', 'cherry', 'grape', 'lemon'] 

print(fruits)

# for i in fruits:
#     print(i)
 

for i, (x) in enumerate(fruits):

    if x == 'cherry':
        x = 'CHERRY'
        print(f' {i + 1} {x}') 

    else:
        print(f' {i + 1} {x}') 