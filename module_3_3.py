

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [5, 7, 12]
values_dict = {'a': 2,'b': 'линия','c': False}
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Столбик']
print_params(*values_list_2, 42)








