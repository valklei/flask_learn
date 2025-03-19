#%%
my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 'sept', 'b': 'oct', 'c': 3}
# Removes and returns the last element of the list
del_element = my_list.pop(0)
print(del_element)
del_elem_dict = my_dict.pop('a')
print(del_elem_dict)
print(my_list)
print(my_dict)