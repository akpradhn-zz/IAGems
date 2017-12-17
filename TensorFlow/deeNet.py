
# Data Set MSNET


# Feed Forward Neural Network Steps
#-----------------------------------------
# input > weight > hidden layer 1 (activation function > weights > hidden l2
# (activation Function)> weight > Output layer)
# Compare Output to intended Output > cost/ loss function (cross entropy)
# optimization function (optimizer) > minimize cost (Adam optimizer, SGD ada Grad)
# Back propagation and update the weight
# Feedforward + backprog = epoch

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/",one_hot=True)

'''
0=[1,0,0,0,0,0,0,0,0,0]
1=[0,1,0,0,0,0,0,0,0,0]
2=[0,0,1,0,0,0,0,0,0,0]
3=[0,0,0,1,0,0,0,0,0,0]
4=[0,0,0,0,1,0,0,0,0,0]
5=[0,0,0,0,0,1,0,0,0,0]
6=[0,0,0,0,0,0,1,0,0,0]
.
.
9=[0,0,0,0,0,0,0,0,0,1]
'''

n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

# Output
n_classes = 10
# Numper of Images
batsize_size = 100

'''
Height * Weight 28*28
Defining shape will be usefull to catch error if size is not of defined shape
'''

x = tf.placeholder('float',[None,784])
y = tf.placeholder('float')

def neural_network_model(data):

	# input data * weight * biasses

	hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784,n_nodes_hl1])),
	                   'biases': tf.Variable(tf.random_normal(n_nodes_hl1))}














