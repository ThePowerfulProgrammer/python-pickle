import pickle 

def write_bin(dict):
    with open('pickle.bin', 'wb') as f:
        pickle.dump(dict,f)

def read_bin(filename):
    with open(filename, 'rb') as f:
        new_dict = pickle.load(f)
        return(new_dict)

print(read_bin('pickle.bin'))