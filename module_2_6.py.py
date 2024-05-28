def print_params (a = 1, b = 'строка', c = True):
    print(a,b,c)
#1
print_params()
print_params(b=25)
print_params(c = [1,2,3])
#2
value_list = [25, 'Denis', [1988,1989]]
value_dict = {'a' : 52,'b' : 'Margo','c':False}
print_params(*value_list)
print_params(**value_dict)
#3
values_list_2 = [54.32,'string']
print_params(*values_list_2,42)



