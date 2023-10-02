print ("Введите первое число:")
a = int(input())
print ("Введите второе число:")
b = int(input())
print ("Сумма этих чисел:", a+b)
print ("Разность этих чисел:", a-b)
print ("Произведение этих чисел:", a*b)
cr = [a,b]
sum = 0
for num in cr:
    sum += num
crednearifm = sum/len(cr)
print ("Среднее арифметическое этих чисел:", crednearifm)
a1 = abs(a)
b1 = abs(b)
max_min = max(a1,b1) - min(a1,b1)
print ("Разность максимального и минимального по модулю:", max_min)
k = a/b
print("Частное чисел с точностью до сотых равно:",f"{k:.2f}")
