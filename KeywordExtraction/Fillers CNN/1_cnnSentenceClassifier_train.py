# STUFF TO INSTALL:
# pip install tensorflow==1.14
# pip install keras==2.2.5

import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Embedding, Conv1D, GlobalMaxPooling1D, MaxPooling1D
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
batch_size, maxlen, epochs = 64, 500, 100
# embedding_dims, filters, kernel_size, hidden_dims = 50, 512, 5, 150
embedding_dims, filters, kernel_size, hidden_dims = 50, 250, 5, 150

# Pad the x sentence vectors to ensure a consistent length
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)

# Vectorize y category values to Keras readable format
y_train = keras.utils.to_categorical(y_train_new, num_classes)

# /////////////////////////////////////////////////////////////////////////////////
# Get x and y validation sets
results = [["x","y"]]

# Code our validation set into numbers (the same numbers used to code the train set)
def codeValidationSet(add_pos_tags=False):
    csvfile = open(os.getcwd() + "/0_validationSet.csv")
    reader = csv.reader(csvfile)
    for row in reader:  # each row is a list
        results.append(row)
    results.remove(["x", "y"])

    x_comments = [i[0] for i in results]

    y_categories = []
    for i in results:
        y_categories.append([i[1]])

    # Turn all y values into ints
    y_validation_new = []
    for list in y_categories:
        for subitem in list:
            y_validation_new.append([int(subitem)])

    encoded_comments = []

    for comment in x_comments:
        originalComment = comment
        comment = nltk.word_tokenize(comment.lower())

        # Create a POS sentence: [ "word", "POS_tag", "word", "POS_tag", ... ]
        if add_pos_tags:
            comment = [ele for word_tuple in nltk.pos_tag(comment) for ele in word_tuple]

        # Turn each comment into a bunch of numbers based on the word embeddings used for training
        encoded_comment = []
        for word in comment:
            if word in word_embedding:
                encoded_comment.append(word_embedding[word])

        encoded_comments.append(encoded_comment)

    # Pad the input vectors to ensure a consistent length
    x_validation = sequence.pad_sequences(encoded_comments, maxlen=maxlen)

    # Vectorize the output sentence type classifications to Keras readable format
    y_validation = keras.utils.to_categorical(y_validation_new, num_classes)

    return x_validation, y_validation

# The x and y validation sets we will use
x_validation, y_validation = codeValidationSet()

# ///////////////////////////////////////////////////
# Training the Actual Model
model = Sequential()

# Created Embedding (Input) Layer (max_words) --> Convolutional Layer
model.add(Embedding(max_words, embedding_dims, input_length=maxlen))
model.add(Dropout(0.2))  # masks various input values

# Create the convolutional layer
model.add(Conv1D(filters, kernel_size, padding='valid', activation='relu', strides=1))

# Create the pooling layer
model.add(MaxPooling1D(pool_size=2, strides=1))

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

# This allows us to plot training and validation set accuracy later on
from keras.callbacks import History
history = History()

# "Fit the model" (train model) using training data (70% of dataset)
model.fit(x_train, y_train, batch_size=batch_size,
          epochs=epochs, validation_data=(x_validation, y_validation), callbacks=[history])

# Save the model to test or use more in the future
model.save('1_myModel.h5')

# ///////////////////////////////////////////////////
# Make a plot of accuracy
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def plot_history(history):
    for key in history.history:
        print (key)

    # In later versions of keras, they use "accuracy" and "val_accuracy" instead of "acc" and "val_acc"
    # May want to check the keys printed in the print statement above when you run

    acc = history.history['acc']
    val_acc = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.savefig('1_trainingValidationAccuracy.png')

plot_history(history)