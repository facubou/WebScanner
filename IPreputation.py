#List IP: Reports, Hostname, Domain, etc from AbuseIPDB
from bs4 import BeautifulSoup
import requests
import re 

dominio = 'https://www.abuseipdb.com/check/107.181.187.5'

webResponse = requests.get(dominio, timeout=5)

contenido = BeautifulSoup(webResponse.content, "html.parser")

contenido = str(contenido).replace("\n", "")

porcentajeRiesgo = re.findall("is <b>(.*?)%", str(contenido))
CantidadReportes = re.findall("reported <b>(.*?)<", str(contenido))
hostname = re.findall("Hostname(s)</th><td>(.*?)\s<", str(contenido))

print(porcentajeRiesgo, CantidadReportes, hostname)

'''
#print(contenido)

contenido2 = str(contenido).replace("\n", "")
w = open("salida4.txt", "w")
w.write(str(contenido2))'''
