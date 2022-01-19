import requests
import bs4
from selenium import webdriver
from zipfile import ZipFile
from io import BytesIO

try:
  webdriver.Chrome()
except:
  f = open("C:\Program Files\Google\Chrome\Application\chrome.VisualElementsManifest.xml", "r")
  parsedManifest = bs4.BeautifulSoup(f.read(), "xml")
  square150x150Logo = parsedManifest.VisualElements.get("Square150x150Logo")
  chromeVersion = square150x150Logo.split('\\')[0]
  print(chromeVersion)
  zip = BytesIO(requests.get('https://chromedriver.storage.googleapis.com/' + chromeVersion + '/chromedriver_win32.zip').content)
  inputZip = ZipFile(zip)
  data = {name: inputZip.read(name) for name in inputZip.namelist()}
  with open('C:\Windows\chromedriver.exe', 'wb') as output:
    output.write(data['chromedriver.exe'])
