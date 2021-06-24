#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

#define a space
blank = " "

#define folder
path = r'/root/loci'

#iterate through all the files
def FilesPath(path):
    filePaths = []
    for root,dirs,files in os.walk(path):
        for file in files:
            filePaths.append(os.path.join(root,file))
    return(filePaths)


def pynorm():
    filePaths = FilesPath(path)
    for file in filePaths:
      f = open(file, encoding='utf-8')
      message = f.read().splitlines()
      for line in message:
          if line.endswith(blank):
             print(line)

      f.close()

if __name__ == "__main__":
    pynorm()
