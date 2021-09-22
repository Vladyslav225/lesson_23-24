# Func(5,  f_n) -> n + nn + nnn = 615
# Func(5,  f_n) -> n + nn + nnn + nnnn = 6170


def sum_number(add_number, number):

     str_number = str(number)

     sums = number

     sum_str = str(number)

     for _ in range(1, add_number):
          sum_str += str_number

          sums += int(sum_str)

     print(sums)


sum_number(4, 5)