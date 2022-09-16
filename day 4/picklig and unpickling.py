import pickle
list = [1,2,3,4,5,6,7,8,9]
file='list.pkl'
print("Made a file")
fileobj=open(file,'wb')
print("ready to write")
pickle.dump(list , fileobj)
print("pickled")
fileobj.close()
print("file closed")

fileobj2=open(file,'rb')
file2=pickle.load(fileobj2)
print("Unpickled a file")
print(file2)
print("printed the file")