# Найдите три ключа с самыми высокими значениями в словаре 
_dict = {'1key':123, '2key':9785, '3key': 560, '4key':234, '5key': 3451}

list_ = []
def func_(_dict):

     # len_ = len(_dict)
     # print(len_)

     for max_value in _dict:
          max_value = max(_dict, key = _dict.get)
          if max_value in _dict:
               list_.append(max_value)
          print(list_)

func_(_dict)
