import numpy as np 
'''
convert dictionary to numpy array!
'''
def dic2np(dic):
    dtype=[]
    length=[]
    for key in dic.keys():
        dic[key]=np.array(dic[key])
        dtype.append(str(dic[key].dtype))
        length.append(len(dic[key]))
    if len(set(length))!=1:raise('Each column of the dictionary does not have the same length')
    # print(dtype)
    # print(dic.keys())
    # print(list(map(tuple,np.array([list(dic.keys()),dtype]).T)))
    return np.array(list(map(tuple,np.array(list((dic.values()))).T)),dtype=list(map(tuple,np.array([list(dic.keys()),dtype]).T)))

