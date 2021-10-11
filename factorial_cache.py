# Факториал числа + кеш


dict_ = {}

def factorial():

     for _ in range(10):
          
          try:

               factorial_number = int(input('Input Number: '))

               if factorial_number in dict_:
                    print(f'Cache {dict_[factorial_number]}')

               elif factorial_number not in dict_:

                    factorial = 1

                    for i in range(1, factorial_number+1):
                         factorial *= i

                    print(f'Fuctorial number {factorial_number} = {factorial}')

                    dict_[factorial_number] = factorial

          except Exception as ex:
               print(ex)
               exit


factorial()


