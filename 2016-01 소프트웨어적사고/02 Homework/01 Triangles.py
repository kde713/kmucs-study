# Made by DongEon Kim

ix = input('Input value of x: ')
iy = input('Input value of y: ')
iz = input('Input value of z: ')

x = float(ix)
y = float(iy)
z = float(iz)

if x+y<z :
    print('3')
elif x*x + y*y < z*z or y*y + z*z < x*x or z*z + x*x < y*y :
    print('2')
elif x*x + y*y == z*z or y*y + z*z == x*x or z*z + x*x == y*y :
    print('1')
else :
    print('0')

