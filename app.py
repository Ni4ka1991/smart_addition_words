#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re
from os import system

alphabet = ' abcdefghijklmnopqrstuvwxyz'

def textFromPDF( path, start = 0, end = 1000 ):
    text = ""                                    #initialisation var text string
    
    pdfFileObj = open( path, 'rb' )                    #open file pwd = path
    
    getPdfFile = PdfFileReader( pdfFileObj )
    
    system( "clear" )
    print( f"PDF: found {getPdfFile.numPages} pages" )

textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 100 )
