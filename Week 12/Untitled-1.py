# Open the data file and read the first line
with open('life-expectancy.csv') as life_expt_file:
    life_expt_file.readline()

    # Extract all the years from the data file and store them in a set
    all_years = set()
    for line in life_expt_file:
        year = line.split(',')[2]
        all_years.add(year)

# Loop until the user enters a valid year
while True:
    # Ask the user to enter a year
    try:
        year_to_find = int(input(f"Enter a year you would like to find data for: "))
    except ValueError:
        print("Invalid input. Please enter a valid year.")
        continue

    # Check if the year is within the data
    if str(year_to_find) in all_years:
        break

    if str(year_to_find).lower() == 'exit':
        print('Program will now exit.')
        break

    else:
        print("Invalid year. Please try again.")
        print(f"Enter a year between {min(all_years)} and {max(all_years)}.")

# initialize variables to hold stats for the year
total_life_exp = 0
num_countries = 0
max_life_exp = -1
min_life_exp = float('inf')
max_country = ''
min_country = ''

# Re-open the data file and search for the entered year
with open('life-expectancy.csv') as life_expt_file:
    life_expt_file.readline()
    for line in life_expt_file:
        line = line.strip()
        life_expt_data = line.split(',')

        if life_expt_data[2] == str(year_to_find):
            life_exp_float = float(life_expt_data[3])
            total_life_exp += life_exp_float
            num_countries += 1

            if life_exp_float > max_life_exp:
                max_life_exp = life_exp_float
                max_country = (life_expt_data[0], life_exp_float)

            if life_exp_float < min_life_exp:
                min_life_exp = life_exp_float
                min_country = (life_expt_data[0], life_exp_float)

# calculate average life expectancy for the year
if num_countries > 0:
    avg_life_exp = total_life_exp / num_countries

    print(f"\n{'-'*60}")
    print(f"Stats for {year_to_find}:")
    print(f"{'-'*60}\n")

    print(f"{'Country':<30}{'Life Expectancy':>20}")
    print(f"{max_country[0]:<40}{max_country[1]:>20.2f}")
    print(f"{min_country[0]:<40}{min_country[1]:>20.2f}")

    print('\n')
    print(f"{'Total life expectancy:':<40}{total_life_exp:>20.2f}")
    print(f"{'Number of countries in the year:':<40}{num_countries:>20}")
    print(f"{'Average life expectancy for the year:':<40}{avg_life_exp:>20.2f}")
    print(f"{'Maximum life expectancy for the year:':<40}{max_life_exp:>20.2f}")
    print(f"{'Minimum life expectancy for the year:':<40}{min_life_exp:>20.2f}")
