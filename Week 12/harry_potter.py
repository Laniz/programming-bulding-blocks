max_opening_weekend = 0
# max_movie_name = 0
max_movie_data = []


with open('harry-potter.txt') as movie_file:
    movie_file.readline()

    for line in movie_file:
        line = line.strip()
        movie_data = line.split(',')

        opening_theathers = int(movie_data[4])
        opening_weekend = int(movie_data[3])


        if opening_theathers < 4000:
            if opening_weekend > max_opening_weekend:
                max_opening_weekend = opening_weekend
                max_movie_data = movie_data

print(f'The movie with the highest opening weekend weekend with less than 4000 theaters was {max_movie_data[0]} with {max_opening_weekend:,} in {max_movie_data[4]} thetrers')






        # release_date_parts = movie_data[5].split(" ")
        

        # if release_date_parts[0] == 'Jul':
        #     print(' ')
        #     print(f'{movie_data[0]} was released on {movie_data[5]}')

        # opening_weekend = int(movie_data[3])

#         if opening_weekend > max_opening_weekend:
#             max_opening_weekend = opening_weekend
#             max_movie_data = movie_data
# # print(' ')
# print(f'Highest opening weekend: {max_movie_name} with ${max_opening_weekend:,}.')
# print(' ')

# print(' ')
# print(f'Movie: {max_movie_data[0]}')
# print(f'Highest opening weekend was ${max_opening_weekend:,}')
# print(f'Released on {max_movie_data[5]}')
# print(f'Lifetime gross of ${int(max_movie_data[1]):,}')
# print(' ')
