# Факториал числа + кеш
# * Выведите список файлов в указанной директории.


dict_ = {}

def factorial():

     while True:

          factorial_number = int(input('Input Number: '))

          if factorial_number in dict_:
               print(f'Cache {dict_[factorial_number]}')

          elif factorial_number not in dict_:

               factorial = 1
               for i in range(1, factorial_number+1):
                    factorial *= i
               print(f'Fuctorial number {factorial_number} "=" {factorial}')

               dict_[factorial_number] = factorial

factorial()


