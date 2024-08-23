immutable_var = tuple_ = (3, 4, 'c', 'd')
print(immutable_var)
#tuple_[0] = 5
#print(tuple_)
#происхоит ошибка, т.к. кортеж неизменяемый тип данных и не поддерживает обращение по элементам.
mutable = list_ =[5, 6, 'a', 'b', 'table']
list_[0] = 4
list_[2] = 'f'
print(mutable)