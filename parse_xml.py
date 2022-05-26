from bs4 import BeautifulSoup
import requests


def parse_xml():
    url = "http://upload.itcollege.ee/~aleksei/test.xml"
    xml_content = requests.get(url).content
    soup = BeautifulSoup(xml_content, 'xml')
    titles = soup.find_all('data')

    for title in titles:
        answer = title.get_text()

    return str(answer.strip())

print(parse_xml())
