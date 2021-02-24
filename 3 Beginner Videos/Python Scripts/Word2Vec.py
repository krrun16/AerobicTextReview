# Python program to generate word vectors using Word2Vec 

# importing all necessary modules 
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings 
  
warnings.filterwarnings(action = 'ignore') 
  
import gensim 
from gensim.models import Word2Vec 
  
#  Reads captioned videos files 
sample = open("Fat-Burning Workout.txt") 
s = sample.read()
#s

f = s.replace("\n", " ")
#f

data = [] 
  
# iterate through each sentence in the file 
for i in sent_tokenize(f): 
    temp = [] 
      
    # tokenize the sentence into words 
    for j in word_tokenize(i): 
        temp.append(j.lower()) 
  
    data.append(temp)

temp