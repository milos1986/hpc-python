import numpy as np
lst = [32, 'safdfas', 'dsfsdf', 2.234]
z = np.array(lst)
print(type(z[0]))
print(z)

oneD_array = np.arange(-2.0, 2.0, step=0.2)
print(oneD_array)



''' Generate another 1D NumPy array containing 11 equally spaced values
 between 0.5 and 1.5. Extract every second element of the array. '''
second_array = np.linspace(start=0.5, stop=1.5, num=11)
print(second_array)

print(second_array[::2])

'''Take some Python string and construct from it NumPy array consisting
 of single characters (a character array).'''
z = 'This is some random string'
np_char_array = np.array(z, dtype='c')
print(type(np_char_array))
print(np_char_array)
