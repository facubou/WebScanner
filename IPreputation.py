from bs4 import BeautifulSoup
import requests
import re
salida = ""
entrada = open("bulk.txt", "r")
export = ""
contador = 0
conteoTotal = 0

for j in entrada:
  conteoTotal = conteoTotal + 1

print(conteoTotal)
print(entrada)

for i in entrada:
  dominio = 'https://www.abuseipdb.com/check/' + i
  dominio = dominio.rstrip('\n')
  print (dominio)
  webResponse = requests.get(dominio, timeout=15)
  contenido = BeautifulSoup(webResponse.content, "html.parser")
  contenido = str(contenido).replace("\n", "")
  porcentajeRiego = re.findall("is <b>(.*?)%", contenido)
  cantidadReportes = re.findall("reported <b>(.*?)<", contenido)
  hostname = re.findall("Hostname\(s\)<\/th><td>(.*?)\s", contenido)
  dominio = re.findall("Domain\sName<\/th><td>(.*?)<", contenido)
  pais = re.findall(r'src="\/img\/blank.gif">(.*?)<\/img>', contenido)
  #porcentajeRiego = str(porcentajeRiego).replace("['", "")
  #linea = str(contenido.find_all(['b', '%']))
  salida = (str(i) + "," + str(porcentajeRiego) + "," + str(cantidadReportes) + "," + str(hostname) + "," + str(dominio) + "," + str(pais)) 
  salida = salida.replace('\n', "")
  export = export + salida + "\n"
  contador = contador + 1
  print ("Completado: " + str(contador) + " de " + str(conteoTotal))
  #for


salida3 = open("salida.txt", "w")
salida3.write(str(export))
salida3.close()
