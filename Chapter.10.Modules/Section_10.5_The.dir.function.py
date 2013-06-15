# program has bug, will not show the the intended content of dir(sys) on
# screen.

import sys      # get list of attributes, in this case, for the sys module

print('dir(sys):')
dir(sys)

print('dir():')
dir()   # get list of attributes for current module

print('a = 5')
a = 5   # create a new variable 'a'

print('dir()')
dir()

print('del a')
del a # delete/remove a name

print('dir()')
dir()
