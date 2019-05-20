import urllib
import bs4
import copy
from bs4 import BeautifulSoup
from urllib import request
#import PyPDF2
#import nltk
#nltk.download()

def making_base(url):
    newUrl=url
    html = urllib.request.urlopen(newUrl).read()   
    soup = BeautifulSoup(html, "lxml")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.body.get_text(separator=' ')
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    splitted_txt=text.split()
    return splitted_txt

polish_url = "https://pl.wikipedia.org/wiki/Polska"

polish_txt=making_base(polish_url)
#print(polish_txt)

english_url = "https://en.wikipedia.org/wiki/England"
english_txt=making_base(english_url)
#print(english_txt)

url = input('Tutaj przekopiuj adres strony\n')
txt=making_base(url)
#print(txt)
polish_cnt=0
english_cnt=0

for x in txt:
    for y in polish_txt:
        if x==y:
            polish_cnt+=1
            #print(x)
            #print(y)
            break
        else:
            polish_cnt+=0
for x in txt:
    for y in english_txt:
        if x==y:
            english_cnt+=1
            #print(x)
            #print(y)
            break
        else:
            english_cnt+=0
print("ilość znalezionych słów na stronie: ", end=' ')
print(len(txt))
print("ilość słów w polskiej bazie: ", end=' ')
print(len(polish_txt))
print("ilość słów w angielskiej bazie: ", end=' ')
print(len(english_txt))
print("ilość znalezionych par słów polskich: ",end=" ")
print(polish_cnt)
print("ilość znalezionych par słów angielskich: ", end=' ')
print(english_cnt)

