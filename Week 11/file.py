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
    year_to_find = input(f"Enter a year you would like to find data for. (Type exit to leave): ")
    
    if year_to_find in all_years:
        break

    if year_to_find.lower() == 'exit':
        # print(' ')
        # print('Program will now exit')
        # print(' ')
        break

    else:
        print("Invalid year. Please try again.")
        print(f'Enter a year between {min(all_years)} and {max(all_years)}')

total_life_exp = 0
num_countries = 0
max_life_exp = -1
min_life_exp = float('inf')
max_data = []
min_data = []


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
                max_data = life_expt_data[0]
                
            if life_exp_float < min_life_exp:
                min_life_exp = life_exp_float
                min_data = life_expt_data[0]


if num_countries > 0:
    avg_life_exp = total_life_exp / num_countries

    print(f"\n{'-'*75}")
    print(f"Max and Min {year_to_find}:")
    print(f"{'-'*75}\n")

    print(f"{'Country':<50}{'Life Expectancy':>20}")
    print(' ')

    print(f"{max_data:<50}{max_life_exp:>20.2f}")
    print(f"{min_data:<50}{min_life_exp:>20.2f}")

    print(f"\n{'-'*75}")
    print(f"Other stats for the {year_to_find} (not country):")
    print(f"{'-'*75}\n")

    print(f"{'Number of countries:':<50}{num_countries:>20}")
    print(f"{'Average life expectancy:':<50}{avg_life_exp:>20.2f}")
    print(f"{'Maximum life expectancy:':<50}{max_life_exp:>20.2f}")
    print(f"{'Minimum life expectancy:':<50}{min_life_exp:>20.2f}")

    # print(f'Country with the highest life expetances is {max_data} with {max_life_exp:.2f}')
    # print(f'Country with the highest life expetances is {min_data} with {min_life_exp:.2f}')
    # print(' ')
    # print(f"Total life expectancy: {total_life_exp:.2f}")
    # print(f"Number of countries in the year: {num_countries}")
    # print(f"Average life expectancy for the year: {avg_life_exp:.2f}")
    # print(f"Maximum life expectancy for the year: {max_life_exp:.2f}")
    # print(f"Minimum life expectancy for the year: {min_life_exp:.2f}")
else:
    print(' ')
    print('Program will now exit')
    print(' ')




