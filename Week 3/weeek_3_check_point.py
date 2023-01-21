age = input('How old are you? ')
age_int = int(age)
next_birthday = age_int + 1 
print(f'Your age at your next birthday is {next_birthday}\n \n')

cartoons = input('How many cartoons do you have? ')
eggs = int(cartoons) * 12
print(f'You have {eggs} eggs \n \n' )

cookies = input('How many cookies do you have? ')
people = input('How many people are they? ')
cookie_per_person = int(cookies) / int(people)
print(f'You each get {cookie_per_person:.3} cookies')