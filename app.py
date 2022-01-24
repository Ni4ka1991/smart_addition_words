#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re
from os import system

alphabet = ' abcdefghijklmnopqrstuvwxyz.'

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



    system( "clear" )
    print( f"PDF: found {pages} pages" )
    print()
    print()
    print( "*" * 20 + " >>> " +"TEXT page 1" + " <<< " + "*" * 20 )
    print()
    print( textProcessed )
    print()
    print( "*" * 18 + " >>> " +"END TEXT" + " <<< " + "*" * 18 )

#    return re.sub( " +", " ", textProcessed )




textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 20 )
