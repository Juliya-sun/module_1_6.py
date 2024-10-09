# my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
#
# print(my_dict)
# print(my_dict['Masha'])
# print(my_dict.get('Misha'))
#
# del my_dict['Egor']
# print(my_dict)
#
# my_dict['Kamila'] = 1981
# my_dict['Artem'] = 1915
# print(my_dict)
#


my_set = {1, 'Яблоко', 42.314}
print(my_set)
print(my_set.add(13))
a = (5, 6, 1.6)
print(my_set.add(a))
print(my_set.discard(1))
print(my_set)


# Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
# Existing value: 2002
# Not existing value: None
# Deleted value: 1999
# Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}
#
# Set: {1, 'Яблоко', 42.314}
# Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}