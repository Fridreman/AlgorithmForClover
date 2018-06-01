import item as item
import requests
from bs4 import BeautifulSoup
from lxml import etree

print(item)

url = 'https://qquack.com/'

r = requests.get(url)


def load_web_page():
    request = requests.get(url)
    return request.text


def contain_data(text):
    soup = BeautifulSoup(text, "html.parser")
    title_response = soup.find('div', {'class': "lh-100 col-md-10 no-padding"})
    return title_response is not None


page = 1
while True:
    data = load_web_page()
    if contain_data(data):
        with open('./' + 'asd', 'w', encoding='utf-8') as output_file:
            output_file.write(data)
            f = open('./' + 'asd')
            f.read()

        break
    else:
        break

f = open('./' + 'asd')
f.read()

#example = item_lxml.xpath('.//div[@class = "nameRus"]/a/text()')[0]
#print etree.tostring(example)