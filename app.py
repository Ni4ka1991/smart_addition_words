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
#print( f"Text[:500] - first 500 symbols of text: \n{text[:500]}" )
#input( "hit enter ..." )

def createVocabulary( text ):
        words = text.split(" ")
        vocabulary = list( set( words ))
        vocabulary.sort()
        return vocabulary

vocabulary = createVocabulary( text )
#print(f"Vocabulary -> \n{vocabulary}" )
#print(f"Vocabulary[:20] -> \n{vocabulary[:20]}" )
#input( "hit enter ..." )

def wordToOneHotVector( word ):
    try:
        index = vocabulary.index( word )
    except:
        index = 0  
    return [0] * index + [1] + ( len( vocabulary ) - index - 1)  * [0]

#print( wordToOneHotVector( "will" ))
#input( "hit enter ..." )

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


for xi in range( len( textAsWords ) - 2 ):
#    print( textAsWords[xi] )
#    print( type( textAsWords[xi] ))
    Xw1 = wordToOneHotVector( textAsWords[xi] )              #first word transform to array
#    print( f"Xw1 type: {type( Xw1 )}" )
#    input( "hit enter ..." )
    Xw1 = wordToOneHotVector( "will" )              #first word transform to array
#    print( f"Xw1 account type: {type( Xw1 )}" )
#    input( "hit enter ..." )
    Xw0 = wordToOneHotVector( textAsWords[xi + 1] )          #second word transform to array
    Xc0 = characterToOneHotVector( textAsWords[xi + 2][0] )  #first character of third word

    Yw0 = wordToOneHotVector( textAsWords[xi + 2] )          #third word


    X_.append( Xw1 + Xw0 + Xc0 )
    Y_.append( Yw0 )

system( "clear" )
#X_ = np.array( X_ )
#Y_ = np.array( Y_ )
print( X_[0], Y_[0] )
print(textAsWords[0],textAsWords[1],textAsWords[2][0],"->", oneHotVectorToWord( Y_[0] ))
print( "*" * 13 )
print(X_[5],Y_[5])
print(textAsWords[5],textAsWords[6],textAsWords[7][0],"->",oneHotVectorToWord(Y_[5]))
#print( textAsWords[0], textAsWords[1], textAsWords[2][0]," -> ", oneHotVectorToWord( Y_[0] ))




