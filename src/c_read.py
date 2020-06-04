from a_preproc_train import f0
from b_preproc_test import f1
import numpy as np

##################### TRAIN DATA ##########################
x_train=[]
y_train=[]
#leer db por linea y separar por indice
f=open("traindata.txt")
a=0
for line in f:
    #line=f.readline()
    ls=line.split(", ")
    #preprocesar indices
    litp=[1,3,5,6,7,8,9,13,14]
    ci=0
    xtrp=[]
    ytrp=[]
    for i in ls:
        r=i
        if(ci in litp):
            r=f0(i,ci)
        ci+=1
        r=int(r)
        if((ci-1)<=13):
            xtrp.append(r)
        elif((ci-1)==14):
            ytrp.append(r)
    x_train.append(xtrp)
    y_train.append(ytrp)
    a+=1
x_train=np.asarray(x_train)
y_train=np.asarray(y_train)
##################### TEST DATA ##########################
x_test=[]
y_test=[]
#leer db por linea y separar por indice
f=open("testdata.txt")
a=0
for line in f:
    #line=f.readline()
    ls=line.split(", ")
    #preprocesar indices
    litp=[1,3,5,6,7,8,9,13,14]
    ci=0
    xtrp=[]
    ytrp=[]
    for i in ls:
        r=i
        if(ci in litp):
            r=f1(i,ci)
        ci+=1
        r=int(r)
        if((ci-1)<=13):
            xtrp.append(r)
        elif((ci-1)==14):
            ytrp.append(r)
    x_test.append(xtrp)
    y_test.append(ytrp)
    a+=1
x_test=np.asarray(x_test)
y_test=np.asarray(y_test)

#################################################