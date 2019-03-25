# pip install tensorflow
# if numpy.core._multiarray_umath failed to import, ugrade numpy!
# pip install --upgrade numpy
import tensorflow as tf

# constant: parameter whose value doesnt change
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = node1 * node2

print(node1)
print(node2)

# ===============================
# session is run to evaluate the nodes

sess = tf.Session()
print(sess.run(node1))
print(sess.run(node2))
print(sess.run([node1, node2]))
print(sess.run(node3))