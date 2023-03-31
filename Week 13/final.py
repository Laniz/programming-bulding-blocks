# windchill = 35.74 + 0.6215(t) - 35.75(?V**0.16) + 0.4275(T(V**0.16))
def wind_chill_cal (x, y ):
    return 35.74 + 0.6215*x - 35.75*y**0.16 + 0.4275*x*y**0.16

#convert c to f
def convertion_c_to_f (z):
    return ((z*9)/5) + 32

#function fo print statements
def print_statment (temp_a, wind_speed_a, wind_chill_a):
    print(f'At temperature {temp_a:.2f}F, and wind speed {wind_speed_a} mph, the windchill is: {wind_chill_a:.2f}F')

#user input
temp = float(input('What is the temperature? '))
unit_check = input('Fahrenheit or Celsius (F/C)? ')

#windspeed also used as the counter
wind_speed = 0

while wind_speed < 59:
    wind_speed += 5

    if unit_check.lower() == 'f':
        a = wind_chill_cal(temp, wind_speed)

        print_statment(temp, wind_speed, a)
        

    elif unit_check.lower() == 'c':
        converted_temp = convertion_c_to_f(temp)
        b = wind_chill_cal(converted_temp, wind_speed,)

        print_statment(converted_temp, wind_speed, b)

    else:
        print(' ')
        print('Wrong input!')
        break
