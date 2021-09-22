# Найдите три ключа с самыми высокими значениями в словаре 
# _dict = {'1key':123, '2key':9785, '3key': 560, '4key':234, '5key': 3451, '6key': 11111}

def search_max_keys(_dict):

     sorted_dict = sorted(_dict, reverse=False, key=_dict.get)
     print(sorted_dict)

     for n in sorted_dict[-3:]:
          print(n)

search_max_keys({'1key':123, '2key':9785, '3key': 560, '4key':234, '5key': 3451, '6key': 11111})