
import tensorflow as tf


#Create a tensor with tf.constant
scalar = tf.constant(1)
scalar


#Check the number of dimensions of a tensor
scalar.ndim



#Creating a vector

vector = tf.constant([1, 2, 5])
vector



#Check the dimension of our vector
vector.ndim



matrix = tf.constant([[10,7],[3, 8]])
matrix


matrix.ndim



#Another matrix
another_matrix = tf.constant([[3,8],[8,3],[4.,0.8]], dtype=tf.float16)
another_matrix








another_matrix.ndim





tensor = tf.constant([[[3, 8],
                       [5, 5]],
                      [[4, 8],
                       [5, 8]],
                      [[6, 0],
                       [7, 8]],
                      [[6, 0],
                       [7, 8]]
                      ])
tensor






tensor.ndim






changeable_tensor = tf.Variable([12, 3])
unchangeable_tensor = tf.constant([[12, 3],[3, 5]])
changeable_tensor, unchangeable_tensor





changeable_tensor[1].assign(12)
changeable_tensor