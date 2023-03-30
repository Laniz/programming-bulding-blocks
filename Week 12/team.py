max_books = 0
min_books = 99999999

max_data = []
min_data = []

choice = input('What book do you want? ')

with open('books_and_chapters.txt') as books_file:
    
    for line in books_file:
        line = line.strip()

        books_data = line.split(':')

        scrip = int(books_data[1])
        # book_name = books_data[0]
        book_loc = books_data[2]

        if book_loc == choice:

            if scrip > max_books:
                max_books = scrip
                max_data = books_data[0]



print(f'the most number of chapters is {max_books} belongs to {max_data}')