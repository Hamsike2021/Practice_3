n = int(input('Введите число: '))
seven, five = '0', '0'
if n % 7 == 0: seven = '1'
if n % 5 == 0: five = '1'
print(f'{seven + five}')
