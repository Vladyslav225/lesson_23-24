# Раздница двух массивов (Уникальные значения)
# Func([1,3,4], [2,4,5]) -> [2, 3, 5]
# Func([1,2,3], [2,4,5]) -> [3, 5]

def create_new_list_1(list_1, list_2):
     list_unique_numbers = []
     
     lists =list_1 + list_2

     for number in lists:
          user_count = lists.count(number)

          if user_count == 1:
               user_count = number

               list_unique_numbers.append(user_count)

     print(list_unique_numbers)


create_new_list_1([1,2,3], [2,4,5])
create_new_list_1([1,3,4], [2,4,5])
