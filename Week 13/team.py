import math

side = ' '

while side != 'exit':
    side = input('What kind of shape do u have? ')
    if side == 'square':
        side_square = int(input('What is the length of the side? '))
        def compute_area_square():
            area = side_square * 4
            # print(area)
            return area

        n = compute_area_square()

        print(n)

    if side == 'rectangle':
        width = int(input('what is the with? '))

        length  = int(input('what is length? '))

        def compute_area_rectangle():
            area_rec = width * length
            return area_rec

        b = compute_area_rectangle()

        print(b)

    if side == 'circle':
        radius = int(input('what is the radius of the circle? '))

        def compute_area_circle():
            area_cir = math.pi * radius * radius
            return area_cir

        c = compute_area_circle()

        print(c)

print('exited')