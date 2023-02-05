first_opt = input('''The cold wakes you up, slowly you open your eyes. You pull out your phone, enter the 
password "open sesame". As soon as you do, your phone dies. Realizing you are all alone in the dark, do you SCREAM for 
help or CRAWL around the cave. ''')

#scream choosen main br
if first_opt.lower() == 'scream':
    first_opt_br_one = input('''You scream as loud as you can, A familiar voices calls back
to you. Relief sweeps over you, knowing you can FOLLOW the voice, but maybe SEARCH fo supplies first? ''')

    #follow chosen br lvl one
    if first_opt_br_one.lower() == 'follow':
        first_opt_br_one_one = input('''You follow the voice, the cave seems to narrow, still in the dark.
CONTINUE on this narrowing path or RETURN where you were? ''')

        #continue chosen br lvl one - one
        if first_opt_br_one_one.lower() == 'continue':
            print(f'''the cave suddedly widdens, light blinding your eyes. You have been found and rescured, 
the joy wakes you up from your dream ''')
         
         #Return chosen br lvl one - two 
        elif first_opt_br_one_one.lower() == 'return':
            print('As you turn around, you feel the ground under you give way. The hypnic jerk immediately wakes you up')

    #search chosen br - lvl one - second option
    elif first_opt_br_one.lower() == 'search':
        first_opt_br_one_two = input('''You feel around in the dark, there is flashlight right next you. Do 
you TURN ON the flash light or search for MORE? ''')


#option if user enters a non provided input.
# elif first_opt.lower() != 'crawl' or 'scream':
#     print(f'''As you "{first_opt.lower()}" aimlessly, the cave crumbles in on you. Your alarm goes off and saves you 
# from your nightmare ''')

#crawl chosen main br
elif first_opt.lower() == 'crawl':
    first_opt_br_two = input('''Luckly you find a door. Some how the door speaks. Says "Silver is the only passage, 
you know the ancient password". "What password!?" You yell. You feel around the door, it feels flimsy enough to be 
forced open. What do you? enter the PASSWORD, PAY, Or BREAK the door?   ''')
    
    #password chosen
    if first_opt_br_two.lower() == 'password':
        first_opt_br_two_one = input('"What is the password!" the door roars ')
        
        #enter password
        count = 0
        while first_opt_br_two_one.lower() != 'open sesame':
            count += 1
            print(f'"You have {5 - count} atempts left! ')
            password = input('"What is the password of the of the ancients, beg for MERCY if you do not know!" ')
            if count == 5:  

                break

            elif password.lower() == 'mercy':
                print(' ')
                print('''"I offer no mercy to mortals!" the door screams. Your alarm rings, you wake up and as 
you unlock your phone you realise that the password was open sesame.''') 
                break

            elif password.lower() == 'open sesame':
                print(' ')
                last_in = input('''The Door accepts your password, and teleports you to your final test, there are
two door, one to your LEFT the other to your Right. Which was do you go? ''')
                break
                print(f'''You walk towards the door on your {last_in.lower()}, knowing its your last test. all this 
can be over. Unfortunely the sound of honking cars wakes you up and its time to get ready for school.''')

    #Pay chosen br 2 lvl 1 two
    if first_opt_br_two.lower() == 'pay':
        first_opt_br_two_two = input


else:
    print('wrong choice game will now end. ')



       
                

        

            

            


