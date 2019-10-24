from bs4 import BeautifulSoup
import requests

dominio = 'URL'

webResponse = requests.get(dominio, timeout=5)

contenido = BeautifulSoup(webResponse.content, "html.parser")

print (contenido)
