a, b, c = float(input('Введите коэфф а: ')), float(input('Введите коэфф b: ')), float(input('Введите коэфф c: '))
D = b ** 2 - 4 * a * c
if D < 0:print('Корней нет')
else:
  if D == 0: print(f'x = {round(-b/2 * a)}')
  else:
    print(f'x1 = {round((-b + D ** 0.5)/ 2 * a)}; x2 = {round((-b - D ** 0.5) / 2 * a)}')
