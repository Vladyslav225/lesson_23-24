# Найдите три ключа с самыми высокими значениями в словаре 
_dict = {'1key':123, '2key':9785, '3key': 560, '4key':234, '5key': 3451}

sorted_dict = sorted(_dict, reverse=False, key=_dict.get)
print(sorted_dict)

del _dict['1key']