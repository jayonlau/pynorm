#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:jayonlau

import os
import sys
from binary  import If_Binary
from exclude_file import Exclude_file

#define a space
blank = " "

#define folder
path = sys.argv[1]

#Create file storage directory


#iterate through all the files
def FilesPath(path):
    filePaths = []
    for root,dirs,files in os.walk(path):
        for file in files:
            if not If_Binary(os.path.join(root,file)):
               if not Exclude_file(os.path.join(root,file)):
                  filePaths.append(os.path.join(root,file))
    return(filePaths)


def pynorm():
    filePaths = FilesPath(path)
    for file in filePaths:
#   print(file)
      f = open(file, encoding='utf-8')
      message = f.read().splitlines()
      count = 0
      for line in message:
          count += 1 
          if line.endswith(blank):
             print("The files with spaces are: %s"%file)
             print("The line of file is: %s"%count)
             print("The message is: %s"%line)
             print("\n")
      f.close()

if __name__ == "__main__":
    pynorm()
