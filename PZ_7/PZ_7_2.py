#Дана строка, состоящая из русских слов, набранных заглавными буквами и разделенных пробелами (одним или несколькими). Преобразовать каждое слово в строке, заменив в нем все последующие вхождения его первой буквы на символ «.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «МИНИ.У». Количество пробелов между словами не изменять.
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