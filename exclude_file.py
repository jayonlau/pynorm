#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:jayonlau


def Exclude_file(file_path):
    '''Eliminate unnecessary documents'''
    file = file_path
    if ".md" in file:
       return True
    elif ".git" in file:
       return True
    elif ".svg" in file:
       return True
    elif ".html" in file:
       return True
    elif ".cc" in file:
       return True
    elif ".ts" in file:
       return True
    elif "LICENSE" in file:
       return True
    elif ".xml" in file:
       return True
    elif ".ai" in file:
       return True
    elif ".ttar" in file:
       return True
    else:
       return False    
