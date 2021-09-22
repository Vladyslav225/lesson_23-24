# Func(5,  f_n) -> n + nn + nnn = 615

f_n = 3
num = 5

num1 = str(num) * (f_n - 1)
num2 = str(num) * f_n
sum_ = num + int(num1) + int(num2)
print(sum_)


# Func(5,  f_n) -> n + nn + nnn + nnnn = 6170
f_n = 4
num = 5

num1 = str(num) * (f_n - 2)
num2 = str(num) * (f_n - 1)
num3 = str(num) * f_n
sum_ = num + int(num1) + int(num2) + int(num3)
print(sum_)