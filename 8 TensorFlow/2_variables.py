# variables allow us to add new trainable parameter to graph

import tensorflow as tf

m = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)

print(m)
print(b)
