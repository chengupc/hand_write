#coding:utf-8
#this is open the minst data, the data will 

import gzip
import pickle
import numpy  as np

data  = gzip.open(./mnist.pkl.gz,'rb')
train_set, valid_set, test_seet = pickle.load(data,encoding='unicode-escape')  

images = np.row_stack((train_set[0],valid_set[0],test_seet[0]))
labes = np.hstack((train_set[1],valid_set[1],test-seet[0]))