#!/usr/bin/python
# -*- coding: utf-8 -*-

import magic
import re
import codecs
 
def is_binary_file_1(file_path):
    '''
    根据text文件数据类型判断是否是二进制文件
    :return: True或False，返回是否是二进制文件
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
 
 
def is_binary_file_2(file_path):
    '''
    根据magic文件的魔术判断是否是二进制文件
    :return: True或False，返回是否是二进制文件
    '''
    mime_kw = 'x-executable|x-sharedlib|octet-stream|x-object'  ###可执行文件、链接库、动态流、对象
    try:
        magic_mime = magic.from_file(file_path, mime=True)
        magic_hit = re.search(mime_kw, magic_mime, re.I)
        if magic_hit:
            return True
        else:
            return False
    except ZeroDivisionError:
        return False
 
def If_Binary(file_path):
    if not is_binary_file_1(file_path):
       if not is_binary_file_2(file_path):
          return False
       else:
          return True
    else:
        return True
