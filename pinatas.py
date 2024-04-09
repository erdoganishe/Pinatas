import itertools
import argparse

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

max_res = 0
# max_ord = []
for index in index_perm:
    (res, ord) = get_result(pin,list(index))
    if (res>max_res):
        max_res = res
    #     max_ord = [ord]

    # if (res==max_res):
    #     max_ord.append(ord)

print(max_res)