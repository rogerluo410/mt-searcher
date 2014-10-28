#!/usr/bin/python
# Filename: extract_go.py

#The convention of input parameter "name" needs to respect like this below:
#name,version
def extract_go(name):

#name='gouuid,bcd29efdea6dde845e4146e0b347d15df3a23957'
 name1 = name.split(',')
 
 exact_couple = [name1[0],name1[1]]

 return exact_couple

