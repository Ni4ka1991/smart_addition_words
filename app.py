#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re
from os import system

alphabet = ' abcdefghijklmnopqrstuvwxyz'

def textFromPDF( path, start = 0, end = 1000 ):
    text = ""                                    #initialisation var text string
    
    pdfFileObj = open( path, 'rb' )                    #open file pwd = path
    my_pdf = PdfFileReader( pdfFileObj )
    
    info   = my_pdf.getDocumentInfo()
    pages  = my_pdf.getNumPages()
    page_1 = my_pdf.getPage( 0 )
    text_1 = page_1.extractText()

    system( "clear" )
    print( f"PDF: found {pages} pages" )
    print( f"Meta-info: {info}" )
    print()
    print()
    print( "*" * 20 + " >>> " +"TEXT page 1" + " <<< " + "*" * 20 )
    print()
    print( text_1 )
    print()
    print( "*" * 18 + " >>> " +"END TEXT" + " <<< " + "*" * 18 )
    print()
#    print( my_pdf.extractText() )

textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 100 )
