# The program creates an neural network that simulates the exclusive OR function with two inputs and one output.

# import numpy
import numpy as np

# Defining activation function
#--------------------------------------------------------------------------
# This function returns the derivative function if deriv == True,
# else return execute the activation function.

def activfun(x, deriv=False):
    if(deriv==True):
        return (x*(1-x))

    return 1/(1+np.exp(-x))


# Input data
# First two column are inout and third value is bias
X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])

# The output of the exclusive OR function follows.

# output data
y = np.array([[0],
             [1],
             [1],
             [0]])

# The seed for the random generator is set so that it will return # the same random numbers each time, which is sometimes
# useful for debugging.

np.random.seed(1)

#synapses
syn0 = 2*np.random.random((3,4)) - 1  # 3x4 matrix of weights ((2 inputs + 1 bias) x 4 nodes in the hidden layer)
syn1 = 2*np.random.random((4,1)) - 1  # 4x1 matrix of weights. (4 nodes x 1 output) - no bias term in the hidden layer.

# training step
#--------------------------------------------------------#
for j in range(100000):

    # Calculate forward through the network.
    l0 = X
    l1 = activfun(np.dot(l0, syn0))
    l2 = activfun(np.dot(l1, syn1))

    # Back propagation of errors using the chain rule.
    l2_error = y - l2
    if(j % 10000) == 0:   # Only print the error every 10000 steps, to save time and limit the amount of output.
        print("Error: " + str(np.mean(np.abs(l2_error))))

    l2_delta = l2_error*activfun(l2, deriv=True)

    l1_error = l2_delta.dot(syn1.T)

    l1_delta = l1_error * activfun(l1,deriv=True)

    #update weights (no learning rate term)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

print("Output after training")
print(l2)

# Test the training model

input = np.array([[0,1,1],[1,1,1]])
t0 = input
t1 = activfun(np.dot(t0, syn0))
t2 = activfun(np.dot(t1, syn1))

print ("\nInput : ")
print(input)
print("\nResult :")
print(t2.astype(int))
