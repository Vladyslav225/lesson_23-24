# Находит в троке числа и добавляет их 
# Func('as123sdasdasd asa sd 5 asdasd 42 234') - > 123+5+42+234
# Func('as1sd3asd44asd asa sd 5 asd 43') - > 1+3+44+5+43

list_ = []

def func_(str_):
     
     for n in str_:
          n.strip()
          if n.isdigit():
              list_.append(int(n))

     s = sum(list_)
     print(s)

func_(input('Input your string: '))