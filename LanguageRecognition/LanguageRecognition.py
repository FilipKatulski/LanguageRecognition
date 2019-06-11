import urllib
import bs4
import copy
from bs4 import BeautifulSoup
from urllib import request
#from tkinter import *
import os.path
import time

def make_base(source):
    #textfile=source
    with open (source, "r", encoding='utf-8') as myfile:
        data=myfile.readlines()
    
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in data for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text=text.replace('1','')
    text=text.replace('2','')
    text=text.replace('3','')
    text=text.replace('4','')
    text=text.replace('5','')
    text=text.replace('6','')
    text=text.replace('7','')
    text=text.replace('8','')
    text=text.replace('9','')
    text=text.replace('0','')
    text=text.replace(',','')
    text=text.replace('.','')
    text=text.replace(':','')
    text=text.replace(';','')
    text=text.replace('(','')
    text=text.replace(')','')
    text=text.replace('[','')
    text=text.replace(']','')
    text=text.replace('{','')
    text=text.replace('}','')
    text=text.replace('"','')
    text=text.replace("„",'')
    text=text.replace("”",'')
    text=text.replace('“','')
    text=text.replace('^','')
    text=text.replace('/','')
    text=text.replace('?','')
    text=text.replace('@','')
    text=text.replace('#','')
    text=text.replace('-',' ')
    text=text.replace('+','')
    text=text.replace('=','')
    text=text.replace('•','')
    text=text.replace('●','')
    text=text.replace('',' ')
    text=text.replace('  ',' ')
    text=text.lower()
    base=text.split()
    return base


def bigram_base(base):
    bi_base=[' ', ' ']
    
    for x in range(len(base)):
        try:
            bi_base.append(base[x]+' '+base[x+1])
        except IndexError:
            pass
    
    #bi_base = list(dict.fromkeys(bi_base))
    return bi_base


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
    text=text.replace('1','')
    text=text.replace('2','')
    text=text.replace('3','')
    text=text.replace('4','')
    text=text.replace('5','')
    text=text.replace('6','')
    text=text.replace('7','')
    text=text.replace('8','')
    text=text.replace('9','')
    text=text.replace('0','')
    text=text.replace(',','')
    text=text.replace('.','')
    text=text.replace(':','')
    text=text.replace(';','')
    text=text.replace('(','')
    text=text.replace(')','')
    text=text.replace('[','')
    text=text.replace(']','')
    text=text.replace('{','')
    text=text.replace('}','')
    text=text.replace('"','')
    text=text.replace("„",'')
    text=text.replace("”",'')
    text=text.replace('“','')
    text=text.replace('^','')
    text=text.replace('/','')
    text=text.replace('?','')
    text=text.replace('@','')
    text=text.replace('#','')
    text=text.replace('-',' ')
    text=text.replace('+','')
    text=text.replace('=','')
    text=text.replace('•','')
    text=text.replace('●','')
    text=text.replace('  ',' ')
    text=text.lower()
    splitted_txt=text.split()
    return splitted_txt


#START

#Checking for existing source .txt files

if os.path.isfile('english.txt')==True: 
    print("English base exist")
    english_txt=["lol", "wire"]
    with open("english.txt", "r", encoding='utf-8') as f:
        for line in f:
            english_txt.append(str(line.strip())) 
else:
    # False
    print("English base doesn't exist, insert name of the source file: ", end=' ')
    source=input()
    english_txt=["lol", "wire"]
    english_txt=make_base(source)
    with open("english.txt", "w", encoding='utf-8') as f:
        for s in english_txt:
            f.write(str(s) +"\n")

print("loaded english word bank")

if os.path.isfile('polish.txt')==True: 
    print("Polish base exist")
    polish_txt=["dziwne","słowa"]
    with open("polish.txt", "r", encoding='utf-8') as f:
        for line in f:
            polish_txt.append(str(line.strip()))
else:
    # False
    print("Polish base doesn't exits, insert name of the source file: ", end=' ')
    source=input()
    polish_txt=["dziwne","słowa"]
    polish_txt=make_base(source)
    with open("polish.txt", "w", encoding='utf-8') as f:
        for s in polish_txt:
            f.write(str(s) +"\n")

print("loaded polish word bank")

proto_polish_bi_txt=bigram_base(polish_txt)
polish_bi_txt=[' ',' ']
proto_english_bi_txt=bigram_base(english_txt)
english_bi_txt=[' ', ' ']
if len(proto_polish_bi_txt)>100000:
    print("Polish bigram base would be too long. \nReduced to first 100.000 elements.\n")
    for y in range(100000):
        polish_bi_txt.append(proto_polish_bi_txt[y])
else:
    polish_bi_txt=copy(proto_polish_bi_txt)

if len(proto_english_bi_txt)>100000:
    print("English bigram base would be too long. \nReduced to first 100.000 elements.\n")
    for y in range(100000):
        english_bi_txt.append(proto_english_bi_txt[y])
else:
    english_bi_txt=copy(proto_english_bi_txt)

polish_bi_txt = dict.fromkeys(polish_bi_txt)
english_bi_txt = dict.fromkeys(english_bi_txt)
polish_txt = dict.fromkeys(polish_txt)
english_txt = dict.fromkeys(english_txt)

print("Amount of words in polish unigram base: ", end=' ')
print(len(polish_txt))
print("Amount of words in english unigram base: ", end=' ')
print(len(english_txt))


print("Amount of words in polish bigram base: ", end=' ')
print(len(polish_bi_txt))
print("Amount of words in english bigram base: ", end=' ')
print(len(english_bi_txt))

#PAGE LOADING AND BASE PREPARING

url = input('Copy website address here: \n')
txt=making_base(url)
bi_txt=bigram_base(txt)
bi_txt=dict.fromkeys(bi_txt)
txt=dict.fromkeys(txt)
polish_cnt=0
english_cnt=0
polish_bi_cnt=0
english_bi_cnt=0

#UNIGRAMS
def unigrams(txt, polish_txt, english_txt):
    polish_cnt=0
    english_cnt=0
    start1=time.time()
    for x in txt:
        for y in polish_txt:
            if x==y:
                polish_cnt+=1
                #print(x)
                #print(y)
                break
            else:
                polish_cnt+=0
    end1=time.time()
    print('Elapsed time:', end=' ')
    print(end1-start1)
    for x in txt:
        for y in english_txt:
            if x==y:
                english_cnt+=1
                #print(x)
                #print(y)
                break
            else:
                english_cnt+=0
    return polish_cnt, english_cnt

start1=time.time()
firstunigram=unigrams(txt, polish_txt, english_txt)
end1=time.time()
print('Elapsed time:', end=' ')
print(end1-start1)
polish_cnt=firstunigram[0]
english_cnt=firstunigram[1]


print("Words found on the website: ", end=' ')
print(len(txt))
print("Amount of unigram pairs in polish: ",end=" ")
print(polish_cnt)
print("Amount of unigram pairs in english: ", end=' ')
print(english_cnt)

#BIGRAMS

def bigrams(bi_txt, polish_bi_txt, english_bi_txt):
    polish_bi_cnt=0
    english_bi_cnt=0
    for x in bi_txt:
        for y in polish_bi_txt:
            if x==y:
                polish_bi_cnt+=1
                #print(x,end='   ')
                #print(y)
                break
            else:
                polish_bi_cnt+=0
    
    for x in bi_txt:
        for y in english_bi_txt:
            if x==y:
                english_bi_cnt+=1
                #print(x, end='   ')
                #print(y)
                break
            else:
                english_bi_cnt+=0
    return polish_bi_cnt, english_bi_cnt
start2=time.time()
firstbigram=bigrams(bi_txt,polish_bi_txt,english_bi_txt)
end2=time.time()
print('Elapsed time:', end=' ')
print(end2-start2)
polish_bi_cnt=firstbigram[0]
english_bi_cnt=firstbigram[1]
print("ilość znalezionych par słów polskich(bigrams): ",end=" ")
print(polish_bi_cnt)
print("ilość znalezionych par słów angielskich(bigrams): ", end=' ')
print(english_bi_cnt)

