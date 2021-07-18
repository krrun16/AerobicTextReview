# STUFF TO INSTALL:
# Python 3.7 (There could be bugs with other versions like 3.8)
# pip install streamlit
# pip install pytube3==10.8.5
# pip install youtube_dl
# pip install deepsegment
# pip install tensorflow==1.14
# pip install keras==2.2.5
# pip install nltk


from deepsegment import DeepSegment
import keras
from keras.preprocessing import sequence
import nltk
import os
import csv

# function to return full text from a file
def getFullText(txtFilename) -> str:
    # Read in a text file one line at a time
    workoutTextFile = open(txtFilename, "r")
    fullText = ""

    for lineText in workoutTextFile:
        # Get rid of the \n
        fullText += lineText.rstrip('\n')+" "

    fullText = fullText.lower()
    return fullText

def codeTextForHTMLHighlighting(originalInputText):
    myWords=originalInputText.split()

    newText=""

    for word in myWords:
        newWord=word[0]+"XYZThisMakesSureHighlightingIsDoneCorrectlyXYZ"+word[1:]+" "
        newText+=newWord

    #remove space at the end
    newText=newText[:-1]
    return newText

# Turn our testing set into an array of numbers (the same numbers used to code the training and validation sets)
def create_word_embedding(comments, wordEmbeddings, add_pos_tags=False):
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

# # If you want to feed in a file
# def highlightFillers(transcriptFilename,transcriptFilenameShort,hasFullTxtFilename):
#     # The default language is 'en' for English
#     segmenter = DeepSegment('en')
#
#     mySentencesData=[]
#
#     txtFilename=""
#     if hasFullTxtFilename:
#         txtFilename=transcriptFilename
#     else:
#         txtFilename = os.getcwd() + "/" + transcriptFilename
#
#     fullText = getFullText(txtFilename=txtFilename)
#
#     thisVideoSentencesArray = segmenter.segment_long(fullText)
#
#     for sentence in thisVideoSentencesArray:
#         mySentencesData.append([sentence, 1])
#
#     # Load in the model we trained earlier
#     model = keras.models.load_model(os.getcwd()+"/1_myModel.h5")
#
#     # Get the word embedding codes from training
#     wordEmbeddingCsvfile=open(os.getcwd()+"/1_wordEmbedding.csv")
#     reader = csv.reader(wordEmbeddingCsvfile)
#     wordEmbeddings={}
#     for row in reader: # each row is a list
#         wordEmbeddings[row[0]]=row[1]
#
#     # ///////////////////////////////////////////////////
#     # Get test sets for x (comments) and y (phrase category)
#     results = mySentencesData
#
#     x_comments = [i[0] for i in results]
#     y_categories = []
#     for i in results:
#         y_categories.append([i[1]])
#
#     encoded_comments, x_test_commentAndEncodedComment = create_word_embedding(x_comments, wordEmbeddings, add_pos_tags=True)
#
#     # Same value from CNN training
#     maxlen=500
#
#     # ///////////////////////////////////////////////////
#     # Get a more detailed accuracy report
#     import xlsxwriter
#     workbook = xlsxwriter.Workbook("Results_Detailed Accuracy/detailedAccuracy_"+transcriptFilenameShort+".xlsx")
#     worksheet = workbook.add_worksheet()
#     worksheet.write_row(0, 0, ["Original Text", "Predicted Category", "Confidence Level"])
#
#     colorTextHTML=fullText
#     numberOfFillers = 0
#
#     for i in range(len(x_test_commentAndEncodedComment)):
#         originalInputText = x_test_commentAndEncodedComment[i][0]
#         inputEncoded = [x_test_commentAndEncodedComment[i][1]]
#         inputEncoded = sequence.pad_sequences(inputEncoded, maxlen=maxlen)
#
#         prediction = model.predict(inputEncoded, batch_size=None, verbose=0, steps=None, callbacks=None,
#                                    max_queue_size=10, workers=1, use_multiprocessing=False)
#         max_index = prediction[0].argmax(axis=0)
#
#         if max_index==1:
#             newText=codeTextForHTMLHighlighting(originalInputText)
#             colorTextHTML = colorTextHTML.replace(originalInputText,
#                                                   ' <span style="background-color:#ffffff" class="filler">' + newText + '</span>')
#             numberOfFillers += 1
#
#         worksheet.write(i + 1, 0, originalInputText)
#         worksheet.write(i + 1, 2, max_index)
#         worksheet.write(i + 1, 3, prediction[0][int(max_index)] * 100)
#
#     workbook.close()
#     return colorTextHTML, numberOfFillers

# If you just want to feed in the transcript as a long string of text
def highlightFillersOnText(fullText):
    # The default language is 'en' for English
    segmenter = DeepSegment('en')

    mySentencesData=[]

    thisVideoSentencesArray = segmenter.segment_long(fullText)

    for sentence in thisVideoSentencesArray:
        mySentencesData.append([sentence, 1])

    # Load in the model we trained earlier
    model = keras.models.load_model(os.getcwd()+"/1_myModel.h5")

    # Get the word embedding codes from training
    wordEmbeddingCsvfile=open(os.getcwd()+"/1_wordEmbedding.csv")
    reader = csv.reader(wordEmbeddingCsvfile)
    wordEmbeddings={}
    for row in reader: # each row is a list
        wordEmbeddings[row[0]]=row[1]

    # ///////////////////////////////////////////////////
    # Get test sets for x (comments) and y (phrase category)
    results = mySentencesData

    x_comments = [i[0] for i in results]
    y_categories = []
    for i in results:
        y_categories.append([i[1]])

    encoded_comments, x_test_commentAndEncodedComment = create_word_embedding(x_comments, wordEmbeddings, add_pos_tags=True)

    # Same value from CNN training
    maxlen=500

    # ///////////////////////////////////////////////////
    # Get a more detailed accuracy report
    import xlsxwriter
    workbook = xlsxwriter.Workbook("Results_Detailed Accuracy/detailedAccuracy.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, ["Original Text", "Predicted Category", "Confidence Level"])

    colorTextHTML=fullText
    numberOfFillers = 0

    for i in range(len(x_test_commentAndEncodedComment)):
        originalInputText = x_test_commentAndEncodedComment[i][0]
        inputEncoded = [x_test_commentAndEncodedComment[i][1]]
        inputEncoded = sequence.pad_sequences(inputEncoded, maxlen=maxlen)

        prediction = model.predict(inputEncoded, batch_size=None, verbose=0, steps=None, callbacks=None,
                                   max_queue_size=10, workers=1, use_multiprocessing=False)
        max_index = prediction[0].argmax(axis=0)

        if max_index==1:
            newText=codeTextForHTMLHighlighting(originalInputText)
            colorTextHTML = colorTextHTML.replace(originalInputText,
                                                  ' <span style="background-color:#ffffff" class="filler">' + newText + '</span>')
            numberOfFillers += 1

        worksheet.write(i + 1, 0, originalInputText)
        worksheet.write(i + 1, 2, max_index)
        worksheet.write(i + 1, 3, prediction[0][int(max_index)] * 100)

    workbook.close()
    return colorTextHTML, numberOfFillers
