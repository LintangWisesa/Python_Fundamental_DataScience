# placeholder allow us to feed data to a tensorflow model from outside model
# it permits a value to be assigned later

import tensorflow as tf

a = tf.placeholder(tf.float32)
b = a * 2

sess = tf.Session()
result = sess.run(b, feed_dict={a: 3})
# feed_dict specifies tensor that provide concrete values to placeholder

print(result)