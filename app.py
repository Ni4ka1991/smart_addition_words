#!/usr/bin/env python3


from PyPDF2 import PdfFileReader
import re

alphabet = ' abcdefghijklmnopqrstuvwxyz'

def textFromPDF( path, start = 0, end = 1000 ):
    text = ""                                    #initialisation var text string
    pdfFileObj = open( path )                    #open file pwd = path
    pdfFileObj.read()

textFromPDF( "./data/Pride-and-Prejudice.pdf", 0, 100 )
