max_salary = 0
min_salary = 99999999999999999999999
#keeping track of the line of data
max_data = []
min_data = []


choice = input('What Job title do you want?')
with open('hr_system.txt') as hr_file:

    for line in hr_file:
        line = line.strip()
        hr_data = line.split(' ')

        salary = int(hr_data[3])
        job_title = hr_data[2]

        if job_title == choice:

            if salary > max_salary:
                max_salary = salary
                #keeping track of the line of data
                max_data = hr_data

            if salary < min_salary:
                min_salary = salary
                #keeping track of line data
                min_data = hr_data

if max_salary != 0:
    print(f'The max salary for {choice} is {max_salary:,} foe {max_data[0]}')
    print(f'the min salary for {choice} is {min_salary:,} for {min_data[0]} ')

else:
    print('Nothing found')

        