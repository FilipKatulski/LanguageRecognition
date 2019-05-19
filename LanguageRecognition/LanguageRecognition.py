import urllib
import bs4
from bs4 import BeautifulSoup
from urllib import request

import PyPDF2
import nltk
#nltk.download()


#pdfFileObject = open('Regulamin.pdf', 'rb')
#pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
#number_of_pages = pdfReader.getNumPages()
#page = pdfReader.getPage(0)
#page_content = page.extractText()
#print(page_content)
def making_base(url):
    newUrl=url
    html = urllib.request.urlopen(newUrl).read()   
    soup = BeautifulSoup(html)

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
    
    #print(text)

    polish_splitted_txt=text.split()
    return polish_splitted_txt

polish_url = "https://pl.wikipedia.org/wiki/Polska"

polish_txt=making_base(polish_url)
#print(polish_txt)

english_url = "https://en.wikipedia.org/wiki/England"
english_txt=making_base(english_url)
#print(english_txt)

url = input('Tutaj przekopiuj adres strony\n')
txt=making_base(url)
print(txt)