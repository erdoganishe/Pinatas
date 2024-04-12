import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import csv

y = []
X = []
with open('trainwith3.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        #print(row)
        y.append(int(str(row).replace(",", "").replace("[", "").replace("]", "").replace(" ", "").replace("'", "").replace(".", "")[-1]))
        tmp_X = []
        for elem in str(row).replace(",", "").replace("[", "").replace("]", "").replace("'", "").replace(".", "").split(" ")[:-1:]:
            tmp_X.append(int(elem))
        X.append(tmp_X)

max_length = max(len(x) for x in X)

X = [x + [0] * (max_length - len(x)) for x in X]

X = np.array(X, dtype=np.int32)
print(X)
y = np.array(y, dtype=np.int32)
#print(y)

model = Sequential()
model.add(Dense(10, input_dim=X.shape[1], activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X, y, epochs=50, batch_size=32)
model.save('my_model_3.h5')

