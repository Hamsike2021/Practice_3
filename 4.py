a, b, c = float(input('Введите коэфф а: ')), float(input('Введите коэфф b: ')), float(input('Введите коэфф c: '))
D = b ** 2 - 4 * a * c
try:
  if D < 0:print('Корней нет')
  else:
    if a == 0 and b != 0 :print(f'x = {round(c / b)}')
    elif a != 0 and b == 0 and c / a >= 0:print(f'x1 = {round(c / a)}; x2 = -{round(c / a)}')
    else:
      if D == 0: print(f'x = {round(-b/2 * a)}')
      else:
        print(f'x1 = {round((-b + D ** 0.5)/ 2 * a)}; x2 = {round((-b - D ** 0.5) / 2 * a)}')
except:
  print('ОШИБКА')
