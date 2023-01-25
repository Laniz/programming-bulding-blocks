import math

m = float(input('Mass (In KG) '))
g = float(input('Gravity in m/s^2, 9.8 for earth, 24 for jupiter: '))
t = float(input('Time (in seconds): '))
p = float(input('Denstity of the fluid (in kg/m3, 1.3 for air, 1000 for water): '))
a = float(input('Cross sectional area (m^2): '))
big_c = float(input ('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

c = (1/2) * (p) * (a) * (big_c)
v_t = math.sqrt((m * g) / c) * (1 - math.exp ((-math.sqrt(m * g * c) / m ) * t ))
t_v = math.sqrt((m * g) / c)
v_t_kph = (v_t * 3600) / 1000


print(f'The inner value of c is {c:.4f}')
print(f'The velocity after {t:.2f} seconds is {v_t:.3f} m/s ')
print(f'The velocity after {t:.2f} seconds is {v_t_kph:.3f} kph ')
print(f'The terminal velocity is {t_v:.2f}')
