#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re
from os import system

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

    textProcessed = text.lower()
    text = textProcessed[:10 ]                  #first 10 symbols of text
    text = text + "д " + text
    print( f"Text with one unalphabet symbol:\n\n\"{text}\"" )
    input( "hit enter" )
    print( f"\nOur string alphabet:\n>>>{alphabet}" )
    for i in text:
        c = alphabet.find( i )
        print( f"\nsymbol {i} found in alphabet in position  {c}" )
        input( "hit enter" )

            

        




    system( "clear" )
    print( f"PDF: found {pages} pages" )
    print()
    print()
    print( "*" * 20 + " >>> " +"TEXT" + " <<< " + "*" * 20 )
    print()
    print( text )
    print()
    print( "*" * 18 + " >>> " +"END TEXT" + " <<< " + "*" * 18 )
    print()

textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 1 )
