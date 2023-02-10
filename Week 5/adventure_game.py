a1 = '''The cold wakes you up, slowly you open your eyes. You pull out your phone, enter the 
password "open sesame". As soon as you do, your phone dies. Realizing you are all alone in the dark, do you SCREAM for 
help or CRAWL around the cave. '''

a2 = '''\nYou scream as loud as you can, A familiar voices calls back
to you. Relief sweeps over you, knowing you can FOLLOW the voice, but maybe SEARCH fo supplies first? '''

a3 = '''\nYou follow the voice, the cave seems to narrow, still in the dark.
CONTINUE on this narrowing path or RETURN where you were? '''

a4  = '''\nthe cave suddedly widdens, light blinding your eyes. You have been found and rescured, 
the joy wakes you up from your dream '''

a5 = '\nAs you turn around, you feel the ground under you give way. The hypnic jerk immediately wakes you up'

a6 = '''\nYou feel around in the dark, there is flashlight right next you. Do 
you TURN ON the flash light or search for MORE? '''

a7 = '''\nLuckly you find a door. Some how the door speaks. Says "Silver is the only passage, 
you know the ancient password". "What password!?" You yell. You feel around the door, it feels flimsy enough to be 
forced open. What do you? enter the PASSWORD, PAY, Or BREAK the door?   '''

a8 = '"What is the password!" the door roars. '

a9 = '"What is the password of the of the ancients, beg for MERCY if you do not know!" '

a10 = '''"I offer no mercy to mortals!" the door screams. Your alarm rings, you wake up and as 
you unlock your phone you realise that the password was open sesame.'''

a11 = '''The Door accepts your password, and teleports you to your final test, there are
two door, one to your LEFT the other to your Right. Which was do you go? '''

a12 = ''

first_opt = input(a1)

#scream choosen main br
if first_opt.lower() == 'scream':
    first_opt_br_one = input(a2)
    #follow chosen br lvl one
    if first_opt_br_one.lower() == 'follow':
        first_opt_br_one_one = input(a3)

        #continue chosen br lvl one - one
        if first_opt_br_one_one.lower() == 'continue':
            print(a4)
         
         #Return chosen br lvl one - two 
        elif first_opt_br_one_one.lower() == 'return':
            print(a5)

    #search chosen br - lvl one - second option
    elif first_opt_br_one.lower() == 'search':
        first_opt_br_one_two = input(a6)

#crawl chosen main br
elif first_opt.lower() == 'crawl':
    first_opt_br_two = input(a7)
    
    #password chosen
    if first_opt_br_two.lower() == 'password':
        first_opt_br_two_one = input(a8)
        
        #enter password
        count = 0
        while first_opt_br_two_one.lower() != 'open sesame':

            
            count += 1
            print(f'"You have {5 - count} atempts left! ')
            print(' ')
            password = input(a9)

            # if password.lower() == 'mercy':
            #     print(' ')
            #     print(a10) 
            #     break     

            if count == 4:
                print('this is your last attempt!! ')

            elif count == 5:  
                print('Just kidding you have failed no more attempts left!. ')
                break
        
            #for some reason it would over look the mercy option unless i did it this way.
            elif password.lower() == 'mercy' or password.lower() == 'mercy':
                print(' ')
                print(a10) 
                break

            elif password.lower() == 'open sesame':
                print(' ')
                last_in = input(a11)
                break
                print(f'''You walk towards the door on your {last_in.lower()}, knowing its your last test. all this 
can be over. Unfortunely the sound of honking cars wakes you up and its time to get ready for school.''')

    #Pay chosen br 2 lvl 1 two
    if first_opt_br_two.lower() == 'pay':
        first_opt_br_two_two = input


# else:
#     print('wrong choice game will now end. ')



       
                

        

            

            


