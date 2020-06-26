import urllib
import bs4
import copy
from bs4 import BeautifulSoup
from urllib import request
import os.path

#make bases for language model

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


if os.path.isfile('french.txt')==True:
    print("French base exist")
    french_txt=["moi", "belle"]
    with open("french.txt", "r", encoding='utf-8') as f:
        for line in f:
            french_txt.append(str(line.strip()))
else:
    # False
    print("French base doesn't exist, insert name of the source file: ", end=' ')
    source=input()
    french_txt=["moi", "belle"]
    french_txt=make_base(source)
    with open("french.txt", "w", encoding='utf-8') as f:
        for s in french_txt:
            f.write(str(s) +"\n")

print("loaded french word bank")


if os.path.isfile('german.txt')==True:
    print("German base exist")
    german_txt=["wir", "sind"]
    with open("german.txt", "r", encoding='utf-8') as f:
        for line in f:
            german_txt.append(str(line.strip()))
else:
    # False
    print("German base doesn't exist, insert name of the source file: ", end=' ')
    source=input()
    german_txt=["wir", "sind"]
    german_txt=make_base(source)
    with open("german.txt", "w", encoding='utf-8') as f:
        for s in german_txt:
            f.write(str(s) +"\n")

print("loaded german word bank")


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

polish_bi_txt=bigram_base(polish_txt)
#polish_bi_txt=[' ',' ']
english_bi_txt=bigram_base(english_txt)
#english_bi_txt=[' ', ' ']
french_bi_txt=bigram_base(french_txt)
#french_bi_txt=[' ', ' ']
german_bi_txt=bigram_base(german_txt)
#german_bi_txt=[' ', ' ']


polish_bi_txt = dict.fromkeys(polish_bi_txt)
english_bi_txt = dict.fromkeys(english_bi_txt)
french_bi_txt = dict.fromkeys(french_bi_txt)
german_bi_txt = dict.fromkeys(german_bi_txt)

polish_txt = dict.fromkeys(polish_txt)
english_txt = dict.fromkeys(english_txt)
french_txt = dict.fromkeys(french_txt)
german_txt = dict.fromkeys(german_txt)

print("Amount of words in polish unigram base: ", end=' ')
print(len(polish_txt))
print("Amount of words in english unigram base: ", end=' ')
print(len(english_txt))
print("Amount of words in french unigram base: ", end=' ')
print(len(french_txt))
print("Amount of words in german unigram base: ", end=' ')
print(len(german_txt))

print('\n')

print("Amount of words in polish bigram base: ", end=' ')
print(len(polish_bi_txt))
print("Amount of words in english bigram base: ", end=' ')
print(len(english_bi_txt))
print("Amount of words in french bigram base: ", end=' ')
print(len(french_bi_txt))
print("Amount of words in german bigram base: ", end=' ')
print(len(german_bi_txt))

#PAGE LOADING AND BASE PREPARING

url = input('Copy website address here: \n')
txt=making_base(url)
bi_txt=bigram_base(txt)
bi_txt=dict.fromkeys(bi_txt)
txt=dict.fromkeys(txt)

polish_cnt=0
english_cnt=0
french_cnt=0
german_cnt=0

polish_bi_cnt=0
english_bi_cnt=0
french_bi_cnt=0
german_bi_cnt=0

#UNIGRAMS
def unigrams(txt, polish_txt, english_txt, french_txt, german_txt):
    polish_cnt=0
    english_cnt=0
    french_cnt=0
    german_cnt=0

    for x in txt:
        if x in polish_txt and x not in english_txt and x not in french_txt and x not in german_txt:
            polish_cnt+=1

        elif x in english_txt and x not in polish_txt and x not in french_txt and x not in german_txt:
            english_cnt+=1
        elif x in french_txt and x not in polish_txt and x not in german_txt and x not in english_txt:
            french_cnt+=1
        elif x in german_txt and x not in polish_txt and x not in french_txt and x not in english_txt:
            german_cnt+=1

    return polish_cnt, english_cnt, french_cnt, german_cnt


firstunigram=unigrams(txt, polish_txt, english_txt, french_txt, german_txt)
polish_cnt=firstunigram[0]
english_cnt=firstunigram[1]
french_cnt=firstunigram[2]
german_cnt=firstunigram[3]

print("\nWords found on the website: ", end=' ')
print(len(txt))
print("Amount of unigram pairs in polish: ",end=" ")
print(polish_cnt)
print("Amount of unigram pairs in english: ", end=' ')
print(english_cnt)
print("Amount of unigram pairs in french: ", end=' ')
print(french_cnt)
print("Amount of unigram pairs in german: ", end=' ')
print(german_cnt)

sum_uni=polish_cnt+english_cnt+french_cnt+german_cnt
polish_prob=polish_cnt/(sum_uni)
english_prob=english_cnt/(sum_uni)
french_prob=french_cnt/(sum_uni)
german_prob=german_cnt/(sum_uni)

if polish_prob > english_prob and polish_prob > french_prob and polish_prob > german_prob:
    print("Acccording to unigrams the website is in polish: probability ", end=' ')
    print(round(polish_prob*100,2), end=' ')
    print('%\n\n')
elif english_prob > polish_prob and english_prob > french_prob and english_prob > german_prob:
    print("Acccording to unigrams the website is in english: probability ", end=' ')
    print(round(english_prob*100,2), end=' ')
    print('%\n\n')
elif french_prob > polish_prob and french_prob > english_prob and french_prob > german_prob:
    print("Acccording to unigrams the website is in french: probability ", end=' ')
    print(round(french_prob*100,2), end=' ')
    print('%\n\n')
elif german_prob > polish_prob and german_prob > english_prob and german_prob > french_prob:
    print("Acccording to unigrams the website is in german: probability ", end=' ')
    print(round(german_prob*100,2), end=' ')
    print('%\n\n')


#BIGRAMS

def bigrams(bi_txt, polish_bi_txt, english_bi_txt, french_bi_txt, german_bi_txt):
    polish_bi_cnt=0
    english_bi_cnt=0
    french_bi_cnt=0
    german_bi_cnt=0
    for x in bi_txt:
        if x in polish_bi_txt and x not in english_bi_txt and x not in french_bi_txt and x not in german_bi_txt:
            polish_bi_cnt+=1
        elif x in english_bi_txt and x not in polish_bi_txt and x not in french_bi_txt and x not in german_bi_txt:
            english_bi_cnt+=1
        elif x in french_bi_txt and x not in polish_bi_txt and x not in english_bi_txt and x not in german_bi_txt:
            french_bi_cnt+=1
        elif x in german_bi_txt and x not in polish_bi_txt and x not in french_bi_txt and x not in english_bi_txt:
            german_bi_cnt+=1

    return polish_bi_cnt, english_bi_cnt, french_bi_cnt, german_bi_cnt

firstbigram=bigrams(bi_txt,polish_bi_txt,english_bi_txt, french_bi_txt, german_bi_txt)
polish_bi_cnt=firstbigram[0]
english_bi_cnt=firstbigram[1]
french_bi_cnt=firstbigram[2]
german_bi_cnt=firstbigram[3]
print("Amount of bigram pairs in polish: ",end=" ")
print(polish_bi_cnt)
print("Amount of bigram pairs in english: ", end=' ')
print(english_bi_cnt)
print("Amount of bigram pairs in french: ",end=" ")
print(french_bi_cnt)
print("Amount of bigram pairs in german: ", end=' ')
print(german_bi_cnt)

sum_bi=polish_bi_cnt+english_bi_cnt+french_bi_cnt+german_bi_cnt
polish_bi_prob=polish_bi_cnt/(sum_bi)
english_bi_prob=english_bi_cnt/(sum_bi)
french_bi_prob=french_bi_cnt/(sum_bi)
german_bi_prob=german_bi_cnt/(sum_bi)


if polish_bi_prob > english_bi_prob and polish_bi_prob > french_bi_prob and polish_bi_prob > german_bi_prob:
    print("Acccording to bigrams the website is in polish: probability ", end=' ')
    print(round(polish_bi_prob*100,2), end=' ')
    print('%\n\n')
elif english_bi_prob > polish_bi_prob and english_bi_prob > french_bi_prob and english_bi_prob > german_bi_prob:
    print("Acccording to bigrams the website is in english: probability ", end=' ')
    print(round(english_bi_prob*100,2), end=' ')
    print('%\n\n')
elif french_bi_prob > polish_bi_prob and french_bi_prob > english_bi_prob and french_bi_prob > german_bi_prob:
    print("Acccording to bigrams the website is in french: probability ", end=' ')
    print(round(french_bi_prob*100,2), end=' ')
    print('%\n\n')
elif german_bi_prob > polish_bi_prob and german_bi_prob > english_bi_prob and german_bi_prob > french_bi_prob:
    print("Acccording to bigrams the website is in german: probability ", end=' ')
    print(round(german_bi_prob*100,2), end=' ')
    print('%\n\n')
