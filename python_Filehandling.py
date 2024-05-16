import os

#Exploring Python's OS Module
#Task 1:Directory Inspector

def list_directory_contents(path):
    try:
        #if os.path.exists(path):
        print(os.listdir(path))
    except FileNotFoundError:
        print("File not located.")
    except IOError as e:
        print(e)

path = "/Users/Administrator"
list_directory_contents(path)

#Task 2:File Size Reporter:

def report_file_sizes(direc):
    try:
        #if os.path.exists(directory)
        for file in os.listdir(direc):
            fpath = os.path.join(direc, file)
            fsize = os.path.getsize(file)
            print(f"File {fpath} is {fsize} bytes.")
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)

#direc = "/python-Sets"
report_file_sizes(".")
from collections import Counter

#Task 3:File Extension Counter

#Tester for looking at files extensions-having problems with this
"""path2 = "python-Rex"
for file in path2:
    filex = os.path.split(path2)
    print(filex)
    filex2 = os.path.splitext(path2)
    print(filex2)"""

"""counts = 0
extens = []
for file in os.listdir(path1):
    exten = os.path.splitext(file)[1]
    print(exten)
    if exten in extens:
        extens[exten] += 1
print(extens)"""

import re

#2. Regex Powered Text Data Processing
#Task 1: Email Extractor

contacts = "/contacts.txt"

def extract_emails():
    p = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}")
    with open("python-Filehandling\contacts.txt", "r") as file:
        f = file.read()
        emails = re.findall(p, f)
    print(emails)

extract_emails()

#3. Advanced Python Data Processing and Analysis Challenge
#Task 1:Travel Blog Sentiment Analysis

#pwords = ["amazing", "enjoy", "beautiful", "breathtaking", "wonderful", "stunning", "mesmerizing", "excellence", "delicious", "enlightening", "fantastic"]
#nwords = ["bad", "poor", "disappointing", "overcrowded", "lackluster", "scarce"]

def search_words():
    pwords = ["amazing", "enjoy", "beautiful", "breathtaking", "wonderful", "stunning", "mesmerizing", "excellence", "delicious", "enlightening", "fantastic"]
    nwords = ["bad", "poor", "disappointing", "overcrowded", "lackluster", "scarce"]

    pword_count = 0
    nword_count = 0
    with open("python-Filehandling/travel_blogs.txt", "r") as file:
        f = file.read()
        words = f.split(".,!?")
        print(words)
    for word in words:
        if word in pwords:
            pword_count += 1
        elif word in nwords:
            nword_count += 1   
        else:
            continue
    print(f"The number of positive words in this file is {pword_count}.") 
    print(f"The number of negative words in this file is {nword_count}.")

search_words()

def analyze_blog_sentiments():
    #w = re.compile(r"[\d?,^°]{2,}")
    x = re.compile(r"[,^Â]{2,}")
    w = re.compile(r"[\d,^°]{2,}")
    with open("python-Filehandling\weather_2020.txt", "r") as file:
        y = file.read()
        words1 = y.split()
        temps = re.findall(w, y)
        print(words1)
        print(temps)
"""def pull_temps():
    temps = []
    with open("python-Filehandling\weather_2020.txt", "r") as file:
        y = file.read()
        print(y)
    for match in re.finditer(r"(\d+)\s*^°", y):
        temps.append(int(match.group(1)))
    for temp in temps:
        print(temps)"""
        
analyze_blog_sentiments()
#pull_temps()
