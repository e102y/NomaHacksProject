import requests
from bs4 import BeautifulSoup as banger
import os

def realRead(real):
    path = './Fake/'
    if(real):
        path = './Real/'
    fs = os.scandir(path)
    alto = []
    for i in fs:
        f = open(i)
        fc = f.read()
        f.close()
        alto.append(fc)
    return alto

def getData():
    a = realRead(False)
    b = realRead(True)
    return (a+b)
def main():
    for i in getData():
        print(i)



#Now for web parsing stuff
def GetWebsiteFromUrl(url):
    html = requests.get(url)
    if(html.status_code >= 300):
        raise Exception('bad url, error code: ', html.status_code)
        return ""
    style = banger(html.text, 'html.parser')
    # kill all script and style elements
    for script in style(["script", "style"]):
        script.extract()
    text = style.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

main()


