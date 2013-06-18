import pickle

# the name of the file where we will store the object
shoplistfile = 'shoplist.data'

# the list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# write to the file
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist    # destroy the shoplist variable

# read back from the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)     # load the object from the file
print(storedlist)
