
# coding: utf-8

# ## Approaches 
# - Lexicon Based approach : 
#    Split the given text into smaller text (Word/ phrases/ sentenses) aka tokenization. 
#    Count the number of word resulting a Bag of Word Model. Look for subjectivity of the small text compared to data base od emotional values for words prerecorded by researchers.
# 
# - Machine Learning : 
# 
# Which approach is Good ?

import sys

import tflearn
from tflearn.data_utils import to_categorical, pad_sequences
from tflearn.datasets import imdb
import matplotlib.pyplot as plt # Histogram
from ggplot import *
import numpy as np
import pandas as pd

print('Python Version: %s' % sys.version.split()[0])





train,test,_ = imdb.load_data(path='imdb.pkl',n_words=1000,valid_portion =0.1)

trainX,trainY = train
testX,testY = test




pd.Series(trainX).tail()




print(list(pd.Series(trainX).iloc[534]) )




pd.Series(trainX).shape




pd.Series(trainY).head(4)



pd.Series(trainY).value_counts()


# ## Preprocessing
# - vectorize the inputs (here using sequence padding)



# Sequence Padding
trainX = pad_sequences( trainX, maxlen=100, value =0.)
testX = pad_sequences(testX, maxlen=100, value =0.)



# Converting Labels(factors) to binary vectors
trainY = to_categorical(trainY,nb_classes=2)
testY = to_categorical(testY,nb_classes=2)



trainY


# ### Network Building


# Input Layer 
# 2 Input Parameters
#   bat_size = None
#   length (sequence length) = 100
net = tflearn.input_data([None, 100])
# Embeded layer
net = tflearn.embedding(net,input_dim = 1000,output_dim=128 )
# LSTM Layer
net = tflearn.lstm(net,128, dropout = 0.8)
# Note : dropout are used to deal with over fitting by randomly turning on/off a neurond in hiddel layer
net = tflearn.fully_connected (net, 2, activation = 'softmax')
net = tflearn.regression(net,
                         optimizer = 'adam',
                         learning_rate = 0.01,
                         loss = 'categorical_crossentropy' )


# Training
model = tflearn.DNN(net, tensorboard_verbose=0)

model.fit(trainX, trainY, validation_set = (testX, testY), show_metric = True, batch_size=5)





