try:
  s = str(input('Введите слово (например МИНИМУМ): ')) #обозначение переменных
  q="."
  b=str()
  max = s[0]
  for c in s: #нахождение конечного резултата
    if c==max:
      b=b+q
    else:
      b=b+c
  b=b[1:]
  print(max, b, sep='') #вывод
except:
  ('Введите слово')