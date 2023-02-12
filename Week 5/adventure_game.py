a00 = 'Game will now end. Wrong input!'

a1 = '''The cold wakes you up, and slowly you open your eyes. You pull out your phone, and enter the 
password "open sesame". As soon as you do, your phone dies. Realizing you are all alone in the dark, do you SCREAM for 
help or CRAWL around the cave? '''

a2 = '''You scream as loud as you can, A familiar voice calls back to you. Relief sweeps 
over you, knowing you can FOLLOW the voice, but maybe SEARCH for supplies first? '''

a3 = '''You follow the voice, the cave seems to narrow, still in the dark. 
CONTINUE on this narrowing path or RETURN where you were? '''

a4  = '''The cave suddenly widens, light blinding your eyes. You have been found and rescued, 
the joy wakes you up from your dream. '''

a5 = 'As you turn around, you feel the ground under you give way. The hypnic jerk immediately wakes you up'

a6 = '''You feel around in the dark, there is a flashlight right next to you. Do you TURN ON 
the flashlight or search for MORE? '''

a7 = '''Luckily you find a door. Somehow the door speaks. Says "Silver is the only passage, 
you know the ancient password". "What password!?" You yell. You feel around the door, it feels flimsy enough to be 
forced open. What do you do? enter the PASSWORD, PAY, Or BREAK the door? '''

a8 = '"What is the password!" the door roars. '

a9 = '"What is the password of the ancients, beg for MERCY if you do not know!" '

a10 = '''"I offer no mercy to mortals!" the door screams. Your alarm rings, you wake up, and as 
you unlock your phone you realize that the password was “open sesame”.'''

a11 = '''The Door accepts your password and teleports you to your final test, there are
two doors, one to your LEFT and the other to your RIGHT. Which way do you go? '''

a12 = 'How much silver do  have you mortal? You search through your pockets'

a13 = '"Just kidding" smirks the door. "You have failed no more attempts left!" The door ends your dream and you wake up.'

a14 = '"Give me silver now" yells the door!. Pay with SILVER or NOTHING? '

a15 = '''The door accepts your payment, unfortunately, the birds outside wake up before you
 see the ending'''

a16 = '''You empty out your pockets, you find 10 silver coins. You pay the door and it opens up as 
you wake up, leaving you questioning reality itself.'''

a17 = 'The door disappears, and you sit in darkness, contemplating the finiteness of life, but your alarm saves you. '

a18 = '''You struggle against the door, Your strength impresses the Door. It asks you to stop before it lets you 
Through. Do you STOP or NOT? '''

a19 = 'The door calls you a worthy mortal, and it lets you through. You sleep blissfully till your alarm goes off. '

a20 = '''The harder you push against the door the studier it becomes. With all that effort, you were slowly sliding across 
the bed, till eventually you are woken up by the fall. '''

a21 = '''Light fills the room. You can clearly see a door markerd "Exit". "it cant be that easy" you say to yourself. 
But yes it is that easy. Exiting wakes you up. '''

a22 = 'You find a button that says, "Push to exit" and that’s what you do. And you wake up disappointed.'

a23 = 'This is your last attempt!! '


first_opt = input(a1)

#scream choosen main br
if first_opt.lower() == 'scream':
    print(' ')
    first_opt_br_one = input(a2)

    #follow chosen br lvl one
    if first_opt_br_one.lower() == 'follow':
        print(' ')
        first_opt_br_one_one = input(a3)

        #continue chosen br lvl one - one
        if first_opt_br_one_one.lower() == 'continue':
            print(' ')
            print(a4)
         
         #Return chosen br lvl one - two 
        elif first_opt_br_one_one.lower() == 'return':
            print(' ')
            print(a5)

        else:
            print(' ')
            print(a00)

    #search chosen br - lvl one - second option
    elif first_opt_br_one.lower() == 'search':
        print(' ')
        first_opt_br_one_two = input(a6)

        if first_opt_br_one_two.lower() == 'turn on':
            print(' ')
            print(a21)

        elif first_opt_br_one_two.lower() == 'more':
            print(' ')
            print(a22)

        else:
            print(' ')
            print(a00)

    else:
        print(' ')
        print(a00)

#crawl chosen main br
elif first_opt.lower() == 'crawl':
    print(' ')
    first_opt_br_two = input(a7)
    
    #password chosen
    if first_opt_br_two.lower() == 'password':
        print(' ')
        first_opt_br_two_one = input(a8)
        
        #enter password
        count = 0

        while first_opt_br_two_one.lower() != 'open sesame':
            count += 1
            print(f'"You have {6 - count} atempts left! ')
            print(' ')

            password = input(a9)

            if count == 4:
                print(' ')
                print(a23)
                print(' ')

            elif count == 5:  
                print(' ')
                print( a13)
                break
        
            #for some reason it would over look the mercy option unless i did it this way.
            elif password.lower() == 'mercy' or password.lower() == 'mercy':
                print(' ')
                print(a10) 
                break

            elif password.lower() == 'open sesame':
                print(' ')
                last_in = input(a11)
                if last_in.lower() == 'left' or last_in.lower() == 'right':
                    print(' ')
                    print(f'''As you head towards the door on your {last_in.lower()}, you wake up because
your body is used to waking up a few minutes before your alarm rings \n''')
                else:
                    print(' ')
                    print(a00)
                break

        if first_opt_br_two_one.lower() == 'open sesame':
            print(' ')
            last_in = input(a11)
            if last_in.lower() == 'left' or last_in.lower() == 'right':
                print(' ')
                print(f'''As you head towards the door on your {last_in.lower()}, you wake up because
your body is used to waking up a few minutes before your alarm rings \n''')
            else:
                print(' ')
                print(a00)

    #Pay chosen br 2 lvl 1 two
    elif first_opt_br_two.lower() == 'pay':
        print(' ')
        first_opt_br_two_two = input(a14)

        if first_opt_br_two_two.lower() == 'silver':
            print(' ')
            print(a16)

        elif first_opt_br_two_two.lower() == 'nothing':
            print(' ')
            print(a17)

        else:
            print(' ')
            print(a00)

    elif first_opt_br_two.lower() == 'break':
        print(' ')
        too_sleepy_to_think_of_a_variable_name = input(a18)

        if too_sleepy_to_think_of_a_variable_name.lower() == 'stop':
            print(' ')
            print(a19)

        elif too_sleepy_to_think_of_a_variable_name.lower() == 'not':
            print(' ')
            print(a20)

        else:
            print(' ')
            print(a00)
    else:
        print(' ')
        print(a00)

else:
    print(' ')
    print(a00)



       
                

        

            

            


