import keras
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding, Conv1D, GlobalMaxPooling1D
import numpy as np
import tensorflow as tf
import nltk
import os
import random
import csv
import numpy as np

def create_word_embedding(comments, add_pos_tags=False):
    '''
    :param comments: List of lists containing all the comments to do word embedding
    :param add_pos_tags: Flag to add parts-of-speech tags to the comment
    :return encoded_comments: Comments in a vectorized list of lists.
    '''

    count = 0
    word_embedding = {}
    encoded_comments = []
    commentAndEncodedComment = []

    for comment in comments:
        originalComment=comment
        # Segment sentence(s) to a list: [ "this", "is", "a", "sentence", "." ]
        # Normalize comment by converting to lowercase, for later mapping
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
        commentAndEncodedComment.append([originalComment,encoded_comment])

    return encoded_comments, commentAndEncodedComment, word_embedding


def encode_and_split_data(comments, data_split=0.8):
    '''
    :param comments: List of lists containing all comments
    :param categories: List containing labeled categories for associated comments
    :param data_split: The ratio of training to testing data (typical 80/20 split)
    :return x_train: Numpy array of encoded training sample(s) (comment)
    :return x_test: Numpy array of encoded testing sample(s) (comment)
    :return y_train: Numpy array of encoded training label (category)
    :return y_test: Numpy array of encoded testing label (category)
    '''

    # Word + Punctuation + POS Tags embedding
    encoded_comments, commentAndEncodedComment, word_embedding = create_word_embedding(comments, add_pos_tags=True)

    # Determine the training sample split point
    splitValue = int(len(encoded_comments) * data_split)

    # Split the dataset into training vs testing datasets
    x_train = np.array(encoded_comments[:splitValue])
    x_test = np.array(encoded_comments[splitValue:])
    x_test_commentAndEncodedComment = commentAndEncodedComment[splitValue:]

    return x_train, x_test, x_test_commentAndEncodedComment, splitValue, word_embedding

# Get train and test sets for x (comments) and y (phrase category)
results = [["x","y"]]

csvfile=open(os.path.split(os.path.abspath(os.getcwd()))[0]+"/Classifications/Cleaned/vids123/Classifications_Vids123_filled_coded.csv")
reader = csv.reader(csvfile)
for row in reader: # each row is a list
    results.append(row)

random.shuffle(results)
results.remove(["x","y"])

x_comments=[i[0] for i in results]
y_categories=[]
for i in results:
    y_categories.append([i[1]])

print(y_categories)

x_train, x_test, x_test_commentAndEncodedComment, splitValue, word_embedding=encode_and_split_data(x_comments,
                                                       data_split=0.8)

y_train = (y_categories[:splitValue])
y_test = (y_categories[splitValue:])

# Turn all y values into ints
y_train_new=[]
for list in y_train:
    for subitem in list:
        y_train_new.append([int(subitem)])

y_test_new=[]
for list in y_test:
    for subitem in list:
        y_test_new.append([int(subitem)])

y_trainInteger=y_train_new
y_testInteger=y_test_new

# Save the word embedding codes for future use if I want to test the same model on a different dataset
with open('wordEmbedding.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in word_embedding.items():
       writer.writerow([key, value])

# Determine the number of categories + default (i.e. sentence types)
num_classes = np.max(y_trainInteger) + 1

max_words, batch_size, maxlen, epochs = 10000, 400, 500, 200
embedding_dims, filters, kernel_size, hidden_dims = 50, 250, 5, 150

# Vectorize the output sentence type classifications to Keras readable format
y_train = keras.utils.to_categorical(y_trainInteger, num_classes)
y_test = keras.utils.to_categorical(y_testInteger, num_classes)

# Pad the input vectors to ensure a consistent length
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

model = Sequential()

# Created Embedding (Input) Layer (max_words) --> Convolutional Layer
model.add(Embedding(max_words, embedding_dims, input_length=maxlen))
model.add(Dropout(0.2))  # masks various input values

# Create the convolutional layer
model.add(Conv1D(filters, kernel_size, padding='valid', activation='relu', strides=1))

# Create the pooling layer
model.add(GlobalMaxPooling1D())

# Create the fully connected layer
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))

# Create the output layer (num_classes)
model.add(Dense(num_classes))
model.add(Activation('softmax'))

# Add optimization method, loss function and optimization value
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])

from keras.callbacks import History
history = History()

# "Fit the model" (train model) using training data (80% of dataset)
model.fit(x_train, y_train, batch_size=batch_size,
          epochs=epochs, validation_data=(x_test, y_test), callbacks=[history])

# Evaluate the trained model, using the test data (20% of the dataset)
score = model.evaluate(x_test, y_test, batch_size=batch_size)

# Print the test score (this may be low since the annotated test set is not completely accurate)
print(score)

# Get a more detailed accuracy report
import xlsxwriter
workbook = xlsxwriter.Workbook('detailedAccuracy.xlsx')
worksheet = workbook.add_worksheet()

for i in range(len(x_test_commentAndEncodedComment)):
    originalInputText=x_test_commentAndEncodedComment[i][0]
    inputEncoded=[x_test_commentAndEncodedComment[i][1]]
    inputEncoded = sequence.pad_sequences(inputEncoded, maxlen=maxlen)

    prediction=model.predict(inputEncoded, batch_size=None, verbose=0, steps=None, callbacks=None, max_queue_size=10,workers=1, use_multiprocessing=False)
    print(prediction)
    max_index = prediction[0].argmax(axis=0)

    worksheet.write_row(i, 0, [originalInputText,max_index,y_testInteger[i][0]])
workbook.close()

# Make a plot of accuracy
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
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
    plt.show()

plot_history(history)

# Save the model to test or use more in the future
model.save('myModel.h5')
