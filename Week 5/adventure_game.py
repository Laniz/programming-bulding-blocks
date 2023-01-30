first_opt = input('''The cold wakes you up, slowly you open your eyes. 
Realizing you are all alone in the dark, do you SCREAM for help or CRAWL around the cave.''')

#scream choosen main br
if first_opt.lower() == 'scream':
    first_opt_br_one = input('''You scream as loud as you can, A familiar voices calls back
to you. Relief sweeps over you, knowing you can FOLLOW the voice, but maybe SEARCH fo supplies first? ''')

    #follow chosen br lvl one
    if first_opt_br_one.lower() == 'follow':
        first_opt_br_one_one = input('''You follow the voice, the cave seems to narrow, still in the dark.
CONTINUE on this narrowing path or RETURN where you were?''')

        #continue chosen br lvl one - one
        if first_opt_br_one_one.lower() == 'continue':
            print(f'''the cave suddedly widdens, light blinding your eyes. You have been found and rescured, 
the joy wakes you up from your dream''')
         
         #Return chosen br lvl one - two 
        elif first_opt_br_one_one.lower() == 'return':
            print('As you turn around, you feel the ground under you give way. The hypnic jerk immediately wakes you up')

    #search chosen br - lvl one - second option
    elif first_opt_br_one.lower() == 'search':
        first_opt_br_one_two = input('''You feel around in the dark, there is flashlight right next you. Do 
you TURN ON the flash light or search for MORE?''')


#option if user enters a non provided input.
elif first_opt != 'sream' or 'crawl':
    print(f'''As you {first_opt} aimlessly, the cave crumbles in on you. Your alarm goes off and saves you 
from your nightmare ''')


