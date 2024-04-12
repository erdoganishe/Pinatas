import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
import csv

model = load_model('my_model.h5')


y = []
X = []
with open('test.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        #print(row)
        y.append(int(str(row).replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace("'", "").replace(".", "")[-1]))
        tmp_X = []
        for elem in str(row).replace(",", "").replace("[", "").replace("]", "").replace("'", "").replace(".", "").split(" ")[:-1:]:
            tmp_X.append(int(elem))
        X.append(tmp_X)

max_length = max(len(x) for x in X)
print(X[0])
X = [x + [0] * (max_length - len(x)) for x in X]

X = np.array(X, dtype=np.int32)
#print(X)
y = np.array(y, dtype=np.int32)
#print(y)


def predict(model, X):
    y_pred = model.predict(X)
    return y_pred

# print(X[0].reshape(1, -1))
# print(y[0])
for i in range (0, 100):
    print(predict(model, X[i].reshape(1, -1)))
    print(y[i])