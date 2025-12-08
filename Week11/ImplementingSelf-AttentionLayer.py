# Reference: https://www.geeksforgeeks.org/deep-learning/attention-layers-in-tensorflow/
# See: https://keras.io/2/api/layers/attention_layers/attention/
# See: https://www.geeksforgeeks.org/artificial-intelligence/ml-attention-mechanism/
# See: https://keras.io/2/api/models/model/
# hSee: ttps://www.geeksforgeeks.org/nlp/types-of-attention-mechanism/
"""

Reference: https://jiachen-ml.medium.com/tensorflow-keras-attention-source-code-line-by-line-explained-ed39a03dc574

As a starter, the paper introduced a group of concepts called:

Query
Key
Value
These concepts originated from information retrieval. Think of these concepts in an online shopping website context. Query(ies) is the search term you type in, Key(s) is the descriptions and titles of individual products the search engine indexed. The Value(s) is product page URLs.

Let’s put these concepts in the context of sequence generation. When using an encoder-decoder model, at each time step of generating a Spanish word the decoder will ask “given my current timestep’s hidden state (Query) , which English word annotation (Key/Value) should I pay attention to?” Again, in the context of Natural Language Processing, key and value are often the same.

"""

import tensorflow as tf

input_shape = (32, 64)  

# Create input tensors for queries, keys, and values
query = tf.keras.Input(shape=input_shape)
key = tf.keras.Input(shape=input_shape)
value = tf.keras.Input(shape=input_shape)

# Create an Attention layer
attention_layer = tf.keras.layers.Attention(use_scale=True)
output = attention_layer([query, key, value])
model = tf.keras.Model(inputs=[query, key, value], outputs=output)
model.summary()