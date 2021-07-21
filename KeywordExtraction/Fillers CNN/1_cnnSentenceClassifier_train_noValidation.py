# STUFF TO INSTALL:
# pip install tensorflow==1.14
# pip install keras==2.2.5

import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding, Conv1D, GlobalMaxPooling1D
import nltk
import os
import random
import csv
import numpy as np

# Turns a sentence like "We are going to do another jumping jack" into an array of numbers, like [1, 3, 6, 14, 17, 21, 25, 31]
# each word in the training dataset corresponds to a number. Then this function will "code" every sentence in the training dataset into an array of numbers
# The CNN will recognize patterns in the numbers
def create_word_embedding(comments, add_pos_tags=False):
    count = 0
    word_embedding = {}
    encoded_comments = []
    commentAndEncodedComment = []

    for comment in comments:
        originalComment = comment

        # Segment sentence(s) to a list: [ "this", "is", "a", "sentence", "." ]
        comment = nltk.word_tokenize(comment.lower())

        # Create a POS sentence: [ "word", "POS_tag", "word", "POS_tag", ... ]
        if add_pos_tags:
            comment = [ele for word_tuple in nltk.pos_tag(comment) for ele in word_tuple]

        # Creating mapping: { "this": 1, "is": 2, ... } & encode each comment
        encoded_comment = []
        for word in comment:
            if word not in word_embedding:
                word_embedding[word] = count
                count += 1
            encoded_comment.append(word_embedding[word])

        encoded_comments.append(encoded_comment)
        commentAndEncodedComment.append([originalComment, encoded_comment])

    return encoded_comments, commentAndEncodedComment, word_embedding

# /////////////////////////////////////////////////////////////////////////////////
# Get train sets for x (sentence or phrase) and y (category)
results = [["x", "y"]]

csvfile = open(os.getcwd() + "/0_trainSet.csv")
reader = csv.reader(csvfile)
for row in reader:
    results.append(row)

random.shuffle(results)
results.remove(["x", "y"])

x_comments = [i[0] for i in results]

y_train = []
for i in results:
    y_train.append([i[1]])

encoded_comments, commentAndEncodedComment, word_embedding = create_word_embedding(x_comments, add_pos_tags=True)

# Turn the x value number arrays into numpy arrays
x_train = np.array(encoded_comments)

# Turn y values into ints
y_train_new = []
for list in y_train:
    for subitem in list:
        y_train_new.append([int(subitem)])

max_words=0

# /////////////////////////////////////////////////////////////////////////////////
# Save the word embedding codes for future use to test the same model on a different dataset
with open('1_wordEmbedding.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in word_embedding.items():
        writer.writerow([key, value])
        max_words+=1

# /////////////////////////////////////////////////////////////////////////////////
# Determine the number of categories + default (i.e. sentence types)
num_classes = np.max(y_train_new) + 1

print(max_words)

# Same values as this tutorial, except using 200 epochs for more training: https://austingwalters.com/convolutional-neural-networks-cnn-to-classify-sentences/
# If you're gonna change batch_size or maxlen, need to update it in 2_cnnSentenceClassifier_test.py as well!!!!!!!
batch_size, maxlen, epochs = 64, 500, 200
# embedding_dims, filters, kernel_size, hidden_dims = 50, 512, 5, 150
embedding_dims, filters, kernel_size, hidden_dims = 50, 250, 5, 150

# Pad the x sentence vectors to ensure a consistent length
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)

# Vectorize y category values to Keras readable format
y_train = keras.utils.to_categorical(y_train_new, num_classes)

# ///////////////////////////////////////////////////
# Training the Actual Model
model = Sequential()

# Created Embedding (Input) Layer (max_words) --> Convolutional Layer
model.add(Embedding(max_words, embedding_dims, input_length=maxlen))
model.add(Dropout(0.2))  # masks various input values

# Create the convolutional layer
model.add(Conv1D(filters, kernel_size, padding='valid', activation='relu', strides=1))

# Create the pooling layer
model.add(GlobalMaxPooling1D())

# Create the convolutional layer
model.add(Conv1D(filters, kernel_size, padding='valid', activation='relu', strides=1))

# Create the pooling layer
model.add(GlobalMaxPooling1D())

# Create the 1st fully connected layer
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))

# Create the output layer (num_classes)
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# Add optimization method, loss function and optimization value
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

# "Fit the model" (train model) using training data (70% of dataset)
model.fit(x_train, y_train, batch_size=batch_size,
          epochs=epochs)

# Save the model to test or use more in the future
model.save('1_myModel.h5')
