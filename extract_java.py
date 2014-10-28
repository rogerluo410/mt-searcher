#!/usr/bin/python
# Filename: extract_java.py

#The convention of input parameter "name" needs to respect like this below:
#org.codehaus.jackson:jackson-core-asl:jar:1.6.2
def extract_java(name):

#name='org.codehaus.jackson:jackson-core-asl:jar:1.6.2'
 name1 = name.split(':')

 exact_couple = [ name1[0]+':'+name1[1],name1[3] ]

 return exact_couple


def extract_java1(name):

#name='jackson-core-asl,1.6.2'
 name1 = name.split(',')

 exact_couple = [ name1[0],name1[1] ]

 return exact_couple


