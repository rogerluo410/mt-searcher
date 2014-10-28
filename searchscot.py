#!/usr/bin/python
# Filename: searchscot.py

import xmlrpclib
import time 
import os
import ast
import extract_ruby
import extract_java
import extract_linux
import extract_go
import search_scotzilla
import sys,getopt

# Regarding command
from optparse import OptionParser
usage = "usage: %prog -f inputfile -o outputfile -r/-j/-l/-g" 
parser = OptionParser(usage=usage) 
parser.add_option("-f", "--file", dest="filename", help="Specify new version file.", metavar="FILE") 
parser.add_option("-o", "--outputfile", dest="outputfile",default="outputfile"+time.strftime("%Y%m%d%H%M%S", time.localtime())+".txt",help="Specify output file.Default convention is outputfile + datetime.", metavar="FILE")
parser.add_option("-r", "--ruby", dest="ruby", action="store_true",default=False, help="Handle name + version of ruby style.") 
parser.add_option("-j", "--java", dest="java", action="store_true",default=False, help="Handle name + version of java style.")
parser.add_option("-l", "--linux", dest="linux",action="store_true",default=False,help="Handle name + version of linux style.")
parser.add_option("-g", "--go", dest="go", action="store_true",default=False, help="Handle name + version of go style.")

(options, args) = parser.parse_args()

count = 0
if options.ruby:
  count = count + 1
if options.java: 
  count = count + 1
if options.linux: 
  count = count + 1
if options.go:
  count = count + 1

if count > 1: 
  parser.error("options -r , -j , -l , -g are mutually exclusive.")
if count == 0:
  parser.error("options -r , -j , -l , -g,one option expected.")

print "Get started with handling ["+options.filename+"] at "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

f_input = open(options.filename)
f_output =file(options.outputfile,'w')

line_input = f_input.readline()

while line_input:
   couple = [None]*5
   if options.ruby:
     couple = extract_ruby.extract_ruby(line_input)
     reponse = search_scotzilla.search(couple[0],couple[1],'VMWsource')
   elif options.java:
     couple = extract_java.extract_java1(line_input)
     couple[1] = couple[1].strip('\r\n')
     couple[1] = couple[1].strip('\n')
     reponse = search_scotzilla.search(couple[0],couple[1].lower(),'VMWsource')
   elif options.linux:
     couple = extract_linux.extract_linux(line_input)
     couple[1] = couple[1].strip('\r\n')
     couple[1] = couple[1].strip('\n')
     reponse = search_scotzilla.search(couple[0],couple[1].lower(),'BaseOS') 
   elif options.go: 
     couple = extract_go.extract_go(line_input)
     couple[1] = couple[1].strip('\r\n')
     couple[1] = couple[1].strip('\n')
     reponse = search_scotzilla.search(couple[0],couple[1].lower(),'VMWsource')
   
   cnt = 0  
   for key,value in reponse.items():
      if key == 'stat' and value =='ok':
         cnt = cnt + 1; 
   if cnt == 1:
      f_output.write(couple[0]+','+couple[1]+','+str(reponse['id'])+'\n')
   elif cnt == 0:    
      f_output.write(couple[0]+','+couple[1]+',None\n')
   elif cnt > 1:
      f_output.write(couple[0]+','+couple[1]+',More\n')
   
   f_output.flush()      
   line_input = f_input.readline() 

f_input.close()
f_output.close()
print "Written into ["+options.outputfile+"]" 
print "Completed ["+options.filename+"] at "+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "---------------------------------------------------"
