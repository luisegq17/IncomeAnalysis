from keras.models import load_model
import numpy as np
from c_read import x_test, y_test

model = load_model('s_model.h5')

c=0
cc=0
for i in x_test:
    i=[[i]]
    x_pred=model.predict_classes(i)
    if(x_pred[0]==y_test[c]):
        cc+=1
    c+=1
pacc=(cc*100)/c

print("Accuracy: "+str(cc)+"/"+str(c)+" -> "+str(pacc)+" %")

#legq