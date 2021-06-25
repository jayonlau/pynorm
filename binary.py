#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:jayonlau

import magic
import re
import codecs
 
def Is_binary(file_path):
    '''
    Judge whether it is a binary file according to the text file data type
    :return: True or False
    '''
    TEXT_BOMS = (
        codecs.BOM_UTF16_BE,
        codecs.BOM_UTF16_LE,
        codecs.BOM_UTF32_BE,
        codecs.BOM_UTF32_LE,
        codecs.BOM_UTF8,
    )
    with open(file_path, 'rb') as file:
        CHUNKSIZE = 8192
        initial_bytes = file.read(CHUNKSIZE)
        file.close()
    #: BOMs to indicate that a file is a text file even if it contains zero bytes.
    return not any(initial_bytes.startswith(bom) for bom in TEXT_BOMS) and b'\0' in initial_bytes
 
 
def Is_magic(file_path):
    '''
    Judge whether it is a binary file according to the magic of magic file
    :return: True or False
    '''
    mime_kw = 'x-executable|x-sharedlib|octet-stream|x-object'
    try:
        magic_mime = magic.from_file(file_path, mime=True)
        magic_hit = re.search(mime_kw, magic_mime, re.I)
        if magic_hit:
            return True
        else:
            return False
    except ZeroDivisionError:
        return False
 
def Is_pdf(file_path):
    '''
    Judge whether it is a PDF file
    :return: True or False
    '''
    file = file_path
    if ".pdf" in file:
       return True
    elif ".PDF" in file:
       return True
    else:
       return False

def If_Binary(file_path):
    if not Is_binary(file_path):
       if not Is_magic(file_path):
          if not Is_pdf(file_path):
             return False
          else:
             return True
       else:
          return True
    else:
        return True
