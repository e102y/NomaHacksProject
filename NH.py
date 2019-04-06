import requests
from bs4 import BeautifulSoup as banger
import os


#reads in the data from the buzzfeed political news set and performs word counting
def strata(real):
    #change fs and fe depending on your os
    fs = "C:/Users/Trent/Desktop/Hack-A-Thon/Horne2017_FakeNewsData/Buzzfeed Political News Dataset/Fake/"
    fe = "_Fake.txt"
    if(real):
        fs = "C:/Users/Trent/Desktop/Hack-A-Thon/Horne2017_FakeNewsData/Buzzfeed Political News Dataset/Real/"
        fe = "_Real.txt"
    wc = dict()
    for i in range(1, 48):
        if(real):
            f = open(fs + str(100+i) + fe, "r")
        else:
            f = open(fs + str(i) + fe, "r")
        fc = f.read()
        fcs = fc.split()
        #fci = map(stringToInt, fcs)
        for i in fcs:
            if i in wc:
                wc[i] += 1
            else:
                wc[i] = 1
        f.close()
    return wc

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
        
#word counts by document
#array of word counts
#tuple with 0 fake 1 real
def encapsulateBuzzfeed():
    #change fs and fe depending on your os
    fs = "C:/Users/Trent/Desktop/Hack-A-Thon/Horne2017_FakeNewsData/Buzzfeed Political News Dataset/Fake/"
    fe = "_Fake.txt"
    arr0 = []
    for i in range(1, 48):
        wc = dict()
        f = open(fs + str(i) + fe, "r")
        fc = f.read()
        fcs = fc.split()
        for i in fcs:
            if i in wc:
                wc[i] += 1
            else:
                wc[i] = 1
        arr0.append(wc)
        f.close()

    arr1 = []
    fs = "C:/Users/Trent/Desktop/Hack-A-Thon/Horne2017_FakeNewsData/Buzzfeed Political News Dataset/Real/"
    fe = "_Real.txt"
    for i in range(1, 48):
        wc = dict()
        f = open(fs + str(100+i) + fe, "r")
        fc = f.read()
        fcs = fc.split()
        #fci = map(stringToInt, fcs)
        for i in fcs:
            if i in wc:
                wc[i] += 1
            else:
                wc[i] = 1
        arr1.append(wc)
        f.close()
    return (arr0, arr1)
def stringToInt(s):
        r = 0
        for i in s:
            r = r*100
        return r
def getData():
    a = realRead(False)
    b = realRead(True)
    return (a+b)
def main():
    '''
    gStrata1 = strata(False)
    for i, j in gStrata1.items():
        if(j > 4 and j < 250):
            print(i, ": ", j)
    gStrata2 = strata(True)
    for i, j in gStrata2.items():
        if(j > 4 and j < 250):
            print(i, ": ", j)
    return (gStrata1, gStrata2)
    '''
    '''
    lStrata = encapsulateBuzzfeed()
    print("Fake: ")
    for i in lStrata[0]:
        for j,k in i.items():
            if(k>1):
                print('\t', j, ": ", k)
    print("Real: ")
    for i in lStrata[1]:
        for j,k in i.items():
            if(k>1):
                print('\t', j, ": ", k)
    '''
    for i in getData():
        print(i)



#class defaultNN:
    
#    def train():

#    def test():

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


