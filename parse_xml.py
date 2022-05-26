from bs4 import BeautifulSoup
import requests
import lxml

def parse_xml():
  url = "http://upload.itcollege.ee/~aleksei/test.xml"
  xml_content = requests.get(url).content
  soup = BeautifulSoup(xml_content,'xml')
  
  # your code here
  
  return result
