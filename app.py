#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re
from os import system
import numpy as np
import torch
#np.set_printoptions( threshold = 20, edgeitems = 3  )


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


def createVocabulary( text ):
        words = text.split(" ")
        vocabulary = list( set( words ))
        vocabulary.sort()
        return vocabulary
#        print( vocabulary[:20] )
#        input( "hit enter" )

def wordToOneHotVector( word ):
    try:
        index = vocabulary.index( word )
        arr = [0] * len( vocabulary )
        arr = np.array( arr )
        arr[ index ] = 1
    except:
        index = 0
        arr = [0] * index
    return arr


def characterToOneHotVector( character ):
    try:
        index = alphabet.index( character )
        arr = [0] * len( alphabet )
        arr = np.array( arr )
        arr[ index ] = 1
    except:
        index = 0
        arr = [0] * index
    return arr

def oneHotVectorToWord( vector ):
    print( "*"*12 )
#    return vocabulary[vector.index(1)]


text = textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 20 )
vocabulary = createVocabulary( text )

#wordToOneHotVector( "account" )
#wordToOneHotVector( "baby" )
#arr = [ 0, 0, 0, 0, 0, 0, 1, 0, 0 ]
#print( oneHotVectorToWord( arr ))

#********
textAsWords_ = text.split( " " )
textAsWords = []

for word in textAsWords_:
    if word != '':
        textAsWords.append( word )

X_ = []
Y_ = []


for xi in range( len( textAsWords ) - 2 ):
    Xw1 = wordToOneHotVector( textAsWords[xi] )
    with np.printoptions( threshold = 20, edgeitems = 3  ):
        print( Xw1 )
    print( type( Xw1 ))
    input( "hit Enter" )
    Xw0 = wordToOneHotVector( textAsWords[xi + 1] )
#    np.set_printoptions( threshold = 20, edgeitems = 3  )
    print( Xw0 )
    print( type( Xw0 ))
    input( "hit Enter" )
    Xc0 = characterToOneHotVector( textAsWords[xi + 2][0] )
    print( Xc0 )
    print( type( Xc0 ))
    input( "hit Enter" )
    
    Yw0 = wordToOneHotVector( textAsWords[xi + 2] )
#    X_.append( "1"+"2"+"3" )
#    Y_.append( Yw0 )

system( "clear" )
#print( X_ )
#print( textAsWords[0], textAsWords[1], textAsWords[2][0]," -> ", oneHotVectorToWord( Y_[0] ))




