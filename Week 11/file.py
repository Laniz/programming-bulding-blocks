year_to_find = input('What year would you like to find? ')


# initialize variables to hold stats for the year
total_life_exp = 0
num_countries = 0
max_life_exp = -1
min_life_exp = float('inf')

with open('life-expectancy.csv') as life_expt_file:
    life_expt_file.readline()  
    for line in life_expt_file:
        line = line.strip()
        life_expt_data = line.split(',')
        if life_expt_data[2] == year_to_find:  
            life_exp_float = float(life_expt_data[3])
            total_life_exp += life_exp_float
            num_countries += 1
            if life_exp_float > max_life_exp:
                max_life_exp = life_exp_float
            if life_exp_float < min_life_exp:
                min_life_exp = life_exp_float

# calculate average life expectancy for the year
if num_countries > 0:
    avg_life_exp = total_life_exp / num_countries
else:
    avg_life_exp = 0

# print stats for the year
print(f"Stats for {year_to_find}:")
print(f"Total life expectancy: {total_life_exp:.2f}")
print(f"Number of countries: {num_countries}")
print(f"Average life expectancy: {avg_life_exp:.2f}")
print(f"Maximum life expectancy: {max_life_exp:.2f}")
print(f"Minimum life expectancy: {min_life_exp:.2f}")
