import keras
from keras.preprocessing import sequence
import nltk
import os
import csv
import numpy as np

# Load in the model we trained earlier
model = keras.models.load_model(os.getcwd()+"/1_myModel.h5")

# Get the word embedding codes
wordEmbeddingCsvfile=open(os.getcwd()+"/1_wordEmbedding.csv")
reader = csv.reader(wordEmbeddingCsvfile)
wordEmbeddings={}
for row in reader: # each row is a list
    wordEmbeddings[row[0]]=row[1]

def create_word_embedding(comments, add_pos_tags=False):
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

        # Turn each comment into a bunch of numbers based on the word embeddings used for training
        encoded_comment = []
        for word in comment:
            if word in wordEmbeddings:
                encoded_comment.append(wordEmbeddings[word])

        encoded_comments.append(encoded_comment)
        commentAndEncodedComment.append([originalComment,encoded_comment])

    return encoded_comments, commentAndEncodedComment

# Get test sets for x (comments) and y (phrase category)
results = [["x","y"]]

csvfile=open(os.getcwd()+"/0_fillerDataset.csv")
reader = csv.reader(csvfile)
for row in reader: # each row is a list
    results.append(row)
results.remove(["x","y"])

x_comments=[i[0] for i in results]

encoded_comments, x_test_commentAndEncodedComment = create_word_embedding(x_comments, add_pos_tags=True)
x_test = np.array(encoded_comments)

# Determine the number of categories + default (i.e. sentence types)
num_classes = 16

maxlen=500
batch_size=400

# Pad the input vectors to ensure a consistent length
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)


# Get a more detailed accuracy report
import xlsxwriter
workbook = xlsxwriter.Workbook('2_detailedAccuracyFillers.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write_row(0,0,["Original Text","Predicted Category","Confidence Level"])

for i in range(len(x_test_commentAndEncodedComment)):
    originalInputText=x_test_commentAndEncodedComment[i][0]
    inputEncoded=[x_test_commentAndEncodedComment[i][1]]
    inputEncoded = sequence.pad_sequences(inputEncoded, maxlen=maxlen)

    prediction=model.predict(inputEncoded, batch_size=None, verbose=0, steps=None, callbacks=None, max_queue_size=10,workers=1, use_multiprocessing=False)
    print(prediction)
    max_index = prediction[0].argmax(axis=0)

    # otherIndices=[i for i, v in enumerate(prediction[0]) if v > 0.0625]
    # if max_index in otherIndices:
    #     otherIndices.remove(max_index)

    worksheet.write(i + 1, 0, originalInputText)
    worksheet.write(i + 1, 1, max_index)
    worksheet.write(i + 1, 2, prediction[0][int(max_index)] * 100)

    # columnValue=3
    # for j in range(len(otherIndices)):
    #     worksheet.write(i + 1, columnValue, otherIndices[j])
    #     worksheet.write(i + 1, columnValue+1, prediction[0][otherIndices[j]] * 100)
    #     columnValue += 2

workbook.close()