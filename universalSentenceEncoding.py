# This gives the sentence most similar to the inputted sentence. Different from what we are trying to do but this
    # is what gave me the idea for the sentence classification convolutional neural network

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import os, sys
from sklearn.metrics.pairwise import cosine_similarity

# get cosine similarity matrix
def cos_sim(input_vectors):
    similarity = cosine_similarity(input_vectors)
    return similarity

# get topN similar sentences
def get_top_similar(sentence, sentence_list, similarity_matrix, topN):
    # find the index of sentence in list
    index = sentence_list.index(sentence)
    # get the corresponding row in similarity matrix
    similarity_row = np.array(similarity_matrix[index, :])
    # get the indices of top similar
    indices = similarity_row.argsort()[-topN:][::-1]
    return [sentence_list[i] for i in indices]


module_url = "https://tfhub.dev/google/universal-sentence-encoder/2" #@param ["https://tfhub.dev/google/universal-sentence-encoder/2", "https://tfhub.dev/google/universal-sentence-encoder-large/3"]

# Import the Universal Sentence Encoder's TF Hub module
embed = hub.Module(module_url)

# Reduce logging output.
tf.logging.set_verbosity(tf.logging.ERROR)

sentences_list = [
    # starting an exercise
    'getting ready',
    'starting with',
    'getting right into it',
    'join me',
    "first we're",
    "start off",
    "push up first",
    "going to start",
    "first exercise",
    "start with",
    "are you ready",
    "you ready here we go",
    "you ready",

    # stopping
    'we are done',
    "we're done",
    "it's over",
    "press pause",

    # duration
    'halfway done',
    'not much left',
    'second',
    "minute",
    "more seconds",
    "seconds left",
    "second break",
    "seconds here",
    "almost done",
    "few more seconds",
    "last round",
    "almost halfway",
    "almost there",

    "Nice work nice work not much left."
]

with tf.Session() as session:
  session.run([tf.global_variables_initializer(), tf.tables_initializer()])
  sentences_embeddings = session.run(embed(sentences_list))

similarity_matrix = cos_sim(np.array(sentences_embeddings))

sentence = "Nice work nice work not much left."
top_similar = get_top_similar(sentence, sentences_list, similarity_matrix, 4)

# printing the list using loop
for x in range(len(top_similar)):
    print(top_similar[x])