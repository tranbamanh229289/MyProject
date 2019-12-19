import numpy as np
from sklearn import preprocessing
import pandas as pd
data=pd.read_csv("weather.csv")
data_train=data.values[:10,1:]
data_test=data.values[10:14,1:]
d=data_train.shape[1]
#Digitize data:
def Standardized (data):
    le = preprocessing.LabelEncoder()
    outlook = le.fit_transform(data[:, 0])
    temp = le.fit_transform(data[:, 1])
    humi = le.fit_transform(data[:, 2])
    wind = le.fit_transform(data[:, 3])
    label = le.fit_transform(data[:, 4])
    x = np.array([outlook, temp, humi, wind]).T
    y = np.array(label)
    return x,y
#Divide data into 2 parts: Train (10 points) and Test (5 ponts)
x_train,y_train=Standardized(data_train)
x_test,y_test=Standardized(data_test)
x_true=x_train[np.where(y_train==1),:].reshape(-1,d-1) # y=1(yes)
x_false=x_train[np.where(y_train==0),:].reshape(-1,d-1) #y=0 (no)

def Prob_attribute(x) :
    list_prob=list()
    for i in x.T :
        freq= np.bincount(i)
        a=np.nonzero(freq)[0]
        p=(freq+1)/(np.sum(freq)+np.max(a)+1)
        list_prob.append(p)
    return list_prob

def Prob_label(x):
    list_prob = list()
    freq = np.bincount(x)
    p = freq / np.sum(freq)
    list_prob.append(p)
    return list_prob

def Multinomial_NB(x_test,prob):
    list_prob = list()
    for i in x_test :
        c = 1
        for j in range(i.size):
            k = i[j]
            c = c* prob[j][k]
        list_prob.append(c)
    return list_prob

prob_true=np.array(Prob_attribute(x_true))
prob_false=np.array(Prob_attribute(x_false))
k=np.array(Prob_label(y_train))
#ratio yes in label
k_true=k[:,1]
#ratio no in label 
k_false=k[:,0]

p_true=Multinomial_NB(x_test,prob_true) *k_true
p_false=Multinomial_NB(x_test,prob_false)*k_false

prob_yes=100*p_true/(p_true+p_false)
prob_no=100*p_false/(p_true+p_false)

list_class=list()
delta=prob_yes-prob_no
for i in delta:
    if i<0:
        list_class.append(0)
    else:
        list_class.append(1)

def correct_ratio (list_class,y_test):
    count=0
    for i in list_class-y_test:
        if i !=0:
            count=count+1
    return (len(x_test)-count)/len(x_test)*100
print ("Output of model:",list_class)
print ("Actual results",y_test)
print ("The exact ratio of the Multinomial NB algorithm is:",correct_ratio(list_class,y_test),"%")
