import csv
import re

all_years = [] # this will eventually hold the dictionaries of each year.

with open("textbreconbeacons.html.txt", "r", encoding="utf-8") as f:
    # a sample text, to be tested with a random sampling before expanding
    # into looping through all the texts.
    text = f.readlines()

for line in text:
    match = re.search("\d\d\d\d", line) # possibly add a leading and trailing space? see what happens in sampling.

    if match:
        the_year = match.group()
        print ("Match found: ", the_year)
        #proof of concept that this search can find the year
        break #it stops looking once it finds the first one
    else:
        continue
        #general testing for other four-digit numbers in the text
        #it keeps going line to line until it does find one.
