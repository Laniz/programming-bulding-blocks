print('Please enter the following information.\n \n ------------------ \n')
first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone = input('Phone  number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')
hair_color = input('Hair color: ')
month = input('Month: ')
eye_color = input('Eye color: ')
training = input('Training: ')
print('The ID Card is: \n \n------------------------- \n')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(f'{job_title.title()} \n ID:{id_number} \n')
print(f'{email.lower()} \n {phone} \n')
# print(f'Hair: {hair_color.capitalize():20} Eyes: {eye_color.capitalize()}')
# print(f'Month: {month.capitalize():20} Training: {training.capitalize()}')
# print(hair_color + '' + '' + eye_color)
# print(month + '' + '' + training)
# print(f'Hair: {hair_color.capitalize()} Eyes: {eye_color.capitalize().rjust(50)}')
# string_len = (len(f'Hair: {hair_color.capitalize()} Eyes: {eye_color.capitalize().rjust(50)}'))
# print(string_len)
# string_len_two = (len(f'Month: {month.capitalize()} Training: {training.capitalize().rjust(50)}'))
# print(string_len_two)
# difference = string_len_two - string_len
# print(50 - difference)
# print(f'Month: {month.capitalize()} Training: {training.capitalize().rjust(50 - difference)}')


# print(len(eye_color.capitalize()))
# print(len(training.capitalize().rjust(30)))



string_len = len(f'Hair: {hair_color.capitalize():20} Eyes: {eye_color.capitalize()}')
# print(f'First string len {string_len}')
string_len_one = len(f'Month: {month.capitalize():20} Training: {training.capitalize()}')
# # print(f'string len two {string_len_one}')
diff = string_len_one - string_len
# print(f'diff = {diff} \n')
spacer = 20 - diff

print((f'Hair: {hair_color.capitalize():20} Eyes: {eye_color.capitalize()}'))
print(f'Month: {month.capitalize():{spacer}} Training: {training.capitalize()}')

