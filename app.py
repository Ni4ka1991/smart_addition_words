#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re
from os import system
import numpy as np
import torch
np.set_printoptions( threshold = 20, edgeitems = 4  )


alphabet = ' abcdefghijklmnopqrstuvwxyz'

def textFromPDF( path, start = 0, end = 1000 ):
    text = ""                                    #initialisation var text string
    
    pdfFileObj = open( path, 'rb' )                    #open file pwd = path
    my_pdf = PdfFileReader( pdfFileObj )
    
    pages  = my_pdf.getNumPages()

    for i in range( start, min( pages, end ) ): # in range( 0 = start, min( num of pages and end == 1000 )
        page = my_pdf.getPage( i )
        text += page.extractText()
        i += 1

    textProcessed = ""

    for i in text.lower():
        c = alphabet.find( i )
        if c == -1:
            textProcessed += " "
        else:
            textProcessed += i

    textProcessed = re.sub( "page", " ", textProcessed )
    textProcessed = re.sub( " +", " ", textProcessed )
    
    return re.sub( " +", " ", textProcessed )

text = textFromPDF("./data/Pride-and-Prejudice.pdf", 0, 200 )

def createVocabulary( text ):
        words = text.split(" ")
        vocabulary = list( set( words ))
        vocabulary.sort()
        return vocabulary

vocabulary = createVocabulary( text )

def wordToOneHotVector( word ):
    try:
        index = vocabulary.index( word )
    except:
        index = 0  
    return [0] * index + [1] + ( len( vocabulary ) - index - 1)  * [0]


def characterToOneHotVector( character ):
    try:
        index = alphabet.index( character )
    except:
        index = 0  
    return [0] * index + [1] + ( len( alphabet ) - index - 1)  * [0]

def oneHotVectorToWord( vector ):
    return vocabulary[vector.index(1)]


text = textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 20 )
vocabulary = createVocabulary( text )


textAsWords_ = text.split( " " )
textAsWords = []

for word in textAsWords_:
    if word != '':
        textAsWords.append( word )

X_ = []
Y_ = []

#transform words and caracters in vectors
for xi in range( len( textAsWords ) - 2 ):
    Xw1 = wordToOneHotVector( textAsWords[xi] )              #first word transform to array
    Xw0 = wordToOneHotVector( textAsWords[xi + 1] )          #second word transform to array
    Xc0 = characterToOneHotVector( textAsWords[xi + 2][0] )  #first character of third word

    Yw0 = wordToOneHotVector( textAsWords[xi + 2] )          #third word

    X_.append( Xw1 + Xw0 + Xc0 )    #create a list of [[word0+word1+caracter0inword2], [word1+word2+caracter0inword3],...,] in vector format
    Y_.append( Yw0 )                #create a list of outputs [[word2], [word3], ... []]

X = torch.tensor( X_, dtype = torch.float32 )
Y = torch.tensor( Y_, dtype = torch.float32 )

system( "clear" )
print("TENSORS")
print(X)
print(X.shape)
print(Y)
print(Y.shape)

#prepare the model
N = 2 * len( vocabulary ) + len( alphabet )
M = len( vocabulary )
D = 256

rate = 0.01




