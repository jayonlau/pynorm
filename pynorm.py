#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from binary  import If_Binary

#define a space
blank = " "

#define folder
path = r'/root/ljy/kubespray'

#iterate through all the files
def FilesPath(path):
    filePaths = []
    for root,dirs,files in os.walk(path):
        for file in files:
            if not If_Binary(os.path.join(root,file)):
               filePaths.append(os.path.join(root,file))
    print(filePaths)
    return(filePaths)


def pynorm():
    filePaths = FilesPath(path)
    for file in filePaths:
      print(file)
      f = open(file, encoding='utf-8')
      message = f.read().splitlines()
      for line in message:
          if line.endswith(blank):
             print(line)
      f.close()

if __name__ == "__main__":
    pynorm()
