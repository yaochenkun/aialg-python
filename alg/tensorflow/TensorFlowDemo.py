import sys
sys.path.append('/usr/lib64/python2.7/site-packages')

import tensorflow as tf
import numpy as np
import os

# def train(modelPath, dataSet):
#
# 	# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
# 	x_data = np.random.rand(100).astype(np.float32)
# 	y_data = x_data * 0.1 + 0.3
#
# 	# Try to find values for W and b that compute y_data = W * x_data + b
# 	# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# 	# figure that out for us.)
# 	W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
# 	b = tf.Variable(tf.zeros([1]))
# 	y = W * x_data + b
#
# 	# Minimize the mean squared errors.
# 	loss = tf.reduce_mean(tf.square(y - y_data))
# 	optimizer = tf.train.GradientDescentOptimizer(0.5)
# 	train = optimizer.minimize(loss)
#
# 	# Before starting, initialize the variables.  We will 'run' this first.
# 	init = tf.global_variables_initializer()
#
# 	# Launch the graph.
# 	sess = tf.Session()
# 	sess.run(init)
#
# 	# Fit the line.
# 	for step in range(201):
# 	    sess.run(train)
# 	    if step % 20 == 0:
# 	        # print(step, sess.run(W), sess.run(b))
# 		pass
# 	# Learns best fit is W: [0.1], b: [0.3]
#
# 	return 'training successfully finished'
#
#
#
# modelPath=sys.argv[1]
# dataSet=sys.argv[2]
#
# print os.getpid()
# print 'modelPath',modelPath
# print 'dataSet',dataSet
# print train(modelPath, dataSet)

import tensorflow as tf

def demoTrain():
    W = tf.Variable([.3], dtype=tf.float32, name='weight')
    b = tf.Variable([-.3], dtype=tf.float32, name='bias')
    x = tf.placeholder(tf.float32)
    linear_model = W * x + b
    y = tf.placeholder(tf.float32)
    loss = tf.reduce_sum(tf.square(linear_model - y))

    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)

    x_train = [1, 2, 3, 4]
    y_train = [0, -1, -2, -3]
    init = tf.global_variables_initializer()

    saver = tf.train.Saver()
    with tf.Session() as sess:
        sess.run(init)
        for i in range(1000):
            sess.run(train, {x:x_train, y:y_train})
        curr_w, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})
        print("W: %s b: %s loss: %s" % (curr_w, curr_b, curr_loss))
        print(sess.run(linear_model, {x:3}))
        save_path = saver.save(sess, "../../model/demo_model.ckpt")

def demoPredict(x_value):
    W = tf.Variable([.3], dtype=tf.float32, name='weight')
    b = tf.Variable([-.3], dtype=tf.float32, name='bias')
    x = tf.placeholder(tf.float32)
    predict = W * x + b
    saver = tf.train.Saver()
    with tf.Session() as sess:
        saver.restore(sess, "../../model/demo_model.ckpt")
        print(sess.run(predict, {x:x_value}))

# if __name__ == "__main__":
#     demoTrain()

if __name__ == '__main__':
    demoPredict(10)

# mypath = os.path.join('apple', 'banana', 'orange')
# print mypath