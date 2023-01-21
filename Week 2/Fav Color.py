user_color = input('What color do you like the most? ') 
#compare user input to red                                         
if user_color.lower() == 'red':
    print(f'\nWhat are the chances? I love red too.')
else:    
    print(f'\nGreat! I love red.')
user_reason = input(f'\nWhy do you like {user_color} ?' )
print(f'\nOh wow that is so interesting! \n')
fav_song = input('What is your favourite song? ')
print(' ')
#added double quotations marks for output
least_fav = input(f'"{fav_song}" is lovely, you have great taste in music!\n\nNow whats one song you absolutely hate? ')
print(' ')
print('Yeah, I can see why you dont like it.')
