import urllib
import bs4
import copy
from bs4 import BeautifulSoup
from urllib import request
from tkinter import *
import os.path
from pathlib import Path


#root=Tk()

#button1 = Button( text='Guzik1', fg = 'red')

#button4 = Button( text='Guzik4', fg = 'blue')
#button1.grid(row = 0, column = 1)

#button4.grid(row = 1, column = 1)
#entry1=Entry(root)
#entry1.grid(row=0,column=0)
#entry2=Entry(root)
#entry2.grid(row =1, column=0)

#root.mainloop()



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
    text=text.replace('"','')
    text=text.replace('^','')
    text=text.replace('/','')
    text=text.replace('?','')
    text=text.replace('@','')
    text=text.replace('#','')
    text=text.replace('-',' ')
    text=text.replace('+','')
    text=text.replace('=','')
    text=text.replace('•','')
    text=text.replace('  ',' ')
    splitted_txt=text.split()
    return splitted_txt

polish_url = "https://pl.wikipedia.org/wiki/Polska"
english_url = "https://en.wikipedia.org/wiki/England"

polish_txt=["dziwne","słowa"]
english_txt=["lol", "wire"]

if os.path.isfile('english.txt')==True: 
    
    print("en exist")
    with open("english.txt", "r", encoding='utf-8') as f:
        for line in f:
            english_txt.append(str(line.strip()))
    
else:
    # False
    print("en doesnt exits")
    english_txt=making_base(english_url)
    with open("english.txt", "w", encoding='utf-8') as f:
        for s in english_txt:
            f.write(str(s) +"\n")

print("loaded english word bank")

if os.path.isfile('polish.txt')==True: 
    
    print("pl exist")
    with open("polish.txt", "r", encoding='utf-8') as f:
        for line in f:
            polish_txt.append(str(line.strip()))
    
else:
    # False
    print("pl doesnt exits")
    polish_txt=making_base(polish_url)
    with open("polish.txt", "w", encoding='utf-8') as f:
        for s in polish_txt:
            f.write(str(s) +"\n")

print("loaded polish word bank")


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

