age_first_rider = int(input('What is the age of the first rider? '))
height_first_rider = int(input('What is the height of the first rider? '))
# second_rider = input('Is there a second rider? (Yes or No) ')

second_rider = input('Is there a second rider (yes or no) ').lower() == 'yes'


can_ride = False



if second_rider:
    # if second_rider.lower() == 'yes':
    #     second_rider = True
    age_sec_rider = int(input('What is the age of the second rider? '))
    height_sec_rider = int(input('What is the height of the second rider? '))

# if (age_first_rider >= 12 and age_sec_rider <= 17) or (age_first_rider >= 12 and age_first_rider <= 17):
#     golden_tic = input('Do you have a golden ticket? Yes or No').lower() == 'yes'
#     if golden_tic:
#         print('You can ride ')


if height_first_rider < 36 or height_sec_rider < 36:
    can_ride = False

elif age_first_rider >= 18 and height_first_rider >= 62:
    can_ride = True

elif second_rider:
    if age_first_rider >= 18 or age_first_rider >= 18:
        can_ride = True

    elif age_first_rider < 18 and age_sec_rider < 18:
        if age_sec_rider >= 12 and age_first_rider >= 12:
            can_ride = True


if can_ride:
    print('You may ride ')
else:
    print('you cannot ride')