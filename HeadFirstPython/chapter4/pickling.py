#Saving objects to disk.
import pickle

try:
    with open('data.out','wb') as mydata:
        pickle.dump([1,2],mydata)
except pickle.PickleError:
    print('Error pickling')




