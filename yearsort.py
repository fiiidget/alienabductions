import csv
import re
import os

all_years = {} # this will eventually hold the dictionaries of each year.
found = (0)
notfound = []
indir = "C:\\Users\\Sarah Hackney\\Documents\\GitHub\\alienabductions\\UFOCasebook_text"
for root, dirs, filenames in os.walk(indir):
    for f in filenames:

        with open(indir+"\\"+str(f), "r", encoding="utf-8") as thisfile:
            # this loops through all the files in the folder listed above one by one
            for body in thisfile:
                match = re.search("\d\d\d\d", body) # possibly add a leading and trailing space? see what happens in sampling.

                if match:
                    the_year = match.group()
                    print ("Match found: ", the_year)
                    #proof of concept that this search can find the year
                    found = (found + 1) #counts how many files have a year in them
                    all_years[the_year] = body
                    #this adds the text as the key to the dictionary. As of right now, it creates duplicates of keys with the same years, and only adds the lines of text up until the one with the date in it.
                    break #it stops looking once it finds the first one

                else:
                    continue

                #general testing for other four-digit numbers in the text
                #it keeps going line to line until it does find one.
print(found, all_years)
