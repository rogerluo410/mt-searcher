#!/usr/bin/python
# Filename: extract_ruby.py
import re

def extract_ruby(name):

 exact_name = ''
 exact_version = '' 

 #stack 1
 stack1_top = 0
 stack1 = [None]*50

 #stack 2
 stack2_top = 0
 stack2 = [None]*50

 flag = 0 #switch 
 for i in range(0,len(name)):
  if flag == 0:  #extract exact name
   if re.match('[0-9a-zA-Z]',name[i]) or ( (name[i]=='-' or name[i]=='_' ) and re.match('[0-9a-zA-Z]',name[i+1] )):
     stack1[stack1_top] = name[i] 
     stack1_top=stack1_top+1
   else:
     flag = 1 #switch to extract version
   
  else: #extract exact version 
     if re.match('.*[=]+',name):
         for j in range(i,len(name)):
           if name[j]=='=':
             m = j+1
             for k in range(m,len(name)):
               if name[k]==',':
                   break
               if re.match('[0-9a-zA-Z]',name[k]) or (name[k]=='.' and re.match('[0-9a-zA-Z]',name[k+1] )): 
                   stack2[stack2_top] = name[k]
                   stack2_top=stack2_top+1
             break
         break
     else:
        if re.match('[0-9a-zA-Z]',name[i]) or (name[i]=='.' and re.match('[0-9a-zA-Z]',name[i+1] )):
                     stack2[stack2_top] = name[i]
                     stack2_top=stack2_top+1

 exact_name = exact_name.join(stack1[0:stack1_top])
 exact_version = exact_version.join(stack2[0:stack2_top])
 exact_couple =[exact_name,exact_version]
 return exact_couple
 

