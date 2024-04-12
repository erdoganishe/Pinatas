import numpy as np
from tensorflow.keras.models import load_model # type: ignore
import itertools
import argparse
import warnings
import os

warnings.filterwarnings('ignore', category=Warning)

class Pinatas:
    def __init__(self, list):
        self.list = list
        self.result = 0
    def remove(self, index):
        if (index>=len(self.list)):
            raise StopIteration()
        elif (len(self.list)==1):
            self.result+=self.list[0]
            del(self.list[0])
        elif (index == 0 and index!=len(self.list)-1):
            self.result += self.list[0]*self.list[1]
            del(self.list[0])
        elif (index == len(self.list)-1 and index != 0):
            self.result += self.list[index]*self.list[index-1]
            del(self.list[index])
        else:
            self.result += self.list[index+1]*self.list[index]*self.list[index-1]
            del(self.list[index])

parser = argparse.ArgumentParser(description='Find the maximum product of a subset of a list of integers')
parser.add_argument('nums', metavar='N', type=int, nargs='+', help='a list of integers')
args = parser.parse_args()

pin = Pinatas(args.nums)
pin_copy = Pinatas(pin.list.copy())
startlist = pin.list.copy()

#Full Permutations

index_perm = []
for i in range(0, len(pin.list)):
    index_perm.append(i)
index_perm = list(itertools.permutations(index_perm))

def get_result(pin, index_order):
    pin2 = Pinatas(pin.list.copy())
    index2 = index_order.copy()

    for i in index_order:
        pin2.remove(i)

        for j in range(0, len(index_order)):

            if i<index_order[j]:
                index_order[j]-=1

    return (pin2.result, index2)

def predict(model, X):
    y_pred = model.predict(X)
    return y_pred

max_res = 0
for index in index_perm:
    (res, ord) = get_result(pin,list(index))
    if (res>max_res):
        max_res = res
        max_ord = ord

#Full NN

model = load_model('my_model.h5')
x = []
x = pin.list.copy()
for i in range(len(x), 7):
    x.append(0)

index_list = []
for i in range(0, len(pin.list)):
    #print(x[i])
    np_x = np.array(x)
    #print(np_x.reshape(1, -1))
    index = predict(model, np_x.reshape(1, -1))
    #print(index)
    index = int(np.round(index))
    #print(index)
    pin.remove(index)
    del(x[index])
    x.append(0)
    index_list.append(index)

index_list_2 = index_list.copy()
#Combined

x = []
x = pin_copy.list.copy()
for i in range(len(x), 7):
    x.append(0)

index_list = []
for i in range(0, len(pin_copy.list)):
    if (len(pin_copy.list)==3):
        #print(pin_copy.list, pin_copy.result)
        break
    #print(x[i])
    np_x = np.array(x)
    #print(np_x.reshape(1, -1))
    index = predict(model, np_x.reshape(1, -1))
    #print(index)
    index = int(np.round(index))
    #print(index)
    pin_copy.remove(index)
    del(x[index])
    x.append(0)
    index_list.append(index)
    

index_perm = []
for i in range(0, 3):
    index_perm.append(i)
index_perm = list(itertools.permutations(index_perm))

max_res_2 = 0
max_ord_2 = []
for index in index_perm:
    (res, ord) = get_result(pin_copy,list(index))
    if (res>max_res_2):
        max_res_2 = res
        max_ord_2 = ord
index_list = index_list + max_ord_2

os.system('cls')

#print("Start: ", startlist)
print("NN Method Result: ")
print(pin.result)
#print(index_list_2)
print("Full Permutation Method: ")
print(max_res)
#print(max_ord)
print("Combined Method: ")
print(pin_copy.result + max_res_2)
#print(index_list)