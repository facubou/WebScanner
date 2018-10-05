import wget
import re
import sys

allhref = ""
allhttp = ""
allLink = ""
url=input("URL: ")

#HTML Download
try:
  filename=wget.download(url)
except IndexError:
  print ("No se puede leer la URL: " + IndexError)

print ("\nSe creó el archivo: "+filename)

print("------------------Hyperlinks------------------\n")
with open(filename) as doc:
    for href in doc:
        if not "href" in href:
           continue
        try:

            href ='href="'+ href.split('"')[1]+'"'+"\n"
            allhref = href + allhref
        except IndexError:
            print

print (allhref)
print ("---------------------------------------------------\n\n")

print ("------------------------SRC------------------------\n")
with open(filename) as doc:
    for http in doc:
        if not "http" in http:
           continue
        try:

            http ='"'+ http.split('"')[1]+'"'+"\n"
            allhttp = http + allhttp
        except IndexError:
            print

print (allhttp)
print ("--------------------------------------------------------\n\n")

print ("------------------------Link Rel------------------------\n")
with open(filename) as doc:
    for link in doc:
        if not "link rel" in link:
           continue
        try:

            link ='"'+ link.split('"')[1]+'"'+"\n"
            allLink = link + allLink
        except IndexError:
            print

print (allLink)
print ("-------------------------------------------------\n\n")

try:
  w = open("export.xml", "w")
  w.write(allhref + allhttp + allLink)
  print("Se creó el archivo XML")
except:
  print("No se puedo generar el archivo XML")
