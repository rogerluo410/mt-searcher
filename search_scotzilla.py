#!/usr/bin/python
# Filename: search_scotzilla.py
import xmlrpclib

def search(name,version,category):
 #The new Scotzilla server URL scotzilla-pivotal.eng.vmware.com
 scotzilla = xmlrpclib.Server("https://scotzilla-pivotal.eng.vmware.com/xmlrpc.cgi").SCOTzilla 
 #Searching for Master Tickets
 reponse = scotzilla.find_master({'name': name,'version': version,'category': category})

 return reponse


