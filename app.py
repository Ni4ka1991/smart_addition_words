#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re
from os import system
import numpy as np

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
        arr = np.array( arr[index] )
    return arr


def characterToOneHotVector( character ):
    try:
        index = alphabet.index( character )
        arr = [0] * len( alphabet )
        arr = np.array( arr )
        arr[ index ] = 1
    except:
        index = 0
        arr = np.array( arr[index] )
    return arr


text = textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 20 )

vocabulary = createVocabulary( text )

wordToOneHotVector( "account" )
wordToOneHotVector( "baby" )



