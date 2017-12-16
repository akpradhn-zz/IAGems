# Note

# Array Manupulation of any size
# Tensorflow
# Function on a tensor

import tensorflow as tf 

# Part 1: Computation Graph
x1 = tf.constant(5)
x2 = tf.constant(6)

# Note : tf.mul is replaced ith tf.multiply
# result = x1 * x2
result = tf.multiply(x1,x2)
print(result)

# Part 2: Tensor Session
#sess = tf.Session()
#print(sess.run(result))
#sess.close()

# To close the session automatically
with tf.Session() as sess:
	output = sess.run(result)
	print(output)
	