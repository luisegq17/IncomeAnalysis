import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from c_read import x_train, y_train, x_test, y_test

model = Sequential()
model.add(Dense(64, input_dim=14, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy']
)

model.fit(x_train, y_train,
    epochs=30,
    batch_size=128
)

score = model.evaluate(x_test, y_test, batch_size=128)
print(score)

model.save('s_model.h5')