import csv
import re
import os
import sys

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

all_years = {} # this will eventually hold the dictionaries of each year.
found = (0)
notfound = []
indir = "C:\\Users\\Sarah Hackney\\Documents\\GitHub\\alienabductions\\UFOCasebook_text"
for root, dirs, filenames in os.walk(indir):
    for f in filenames:

        with open(indir+"\\"+str(f), "r", encoding="utf-8") as thisfile:
            # this loops through all the files in the folder listed above one by one
            clean = thisfile.read().replace('\n', '')
            # for body in clean:

            match = re.search("\d\d\d\d", clean) # possibly add a leading and trailing space? see what happens in sampling.

            if match:
                the_year = match.group()
                print ("Match found: ", the_year)
                #proof of concept that this search can find the year
                found = (found + 1) #counts how many files have a year in them
                all_years[the_year] = clean
                #this adds the text as the key to the dictionary. As of right now, it creates duplicates of keys with the same years
                # break #it stops looking once it finds the first one

            else:
                continue

            #general testing for other four-digit numbers in the text
            #it keeps going line to line until it does find one.
uprint(found, all_years)
