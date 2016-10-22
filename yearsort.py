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
        # this is a wrapper function that helps with printing unicode characters. It's not super necessary when writing to files, but prevent unicode-related errors when printing test runs. Thanks to Jelle Fresen on Stackoverflow, via Eugene Rutigliano.

all_years = {} # this is the dictionary that will eventually hold the lists of texts from each year.
indir = "C:\\Users\\Sarah Hackney\\Documents\\GitHub\\alienabductions\\UFOCasebook_text"
for root, dirs, filenames in os.walk(indir):
    for f in filenames:

        with open(indir+"\\"+str(f), "r", encoding="utf-8") as thisfile:
            # this loops through all the files in the above folder listed above one by one
            clean = thisfile.read().replace('\n', '')
            # this gets rid of the linebreaks in the docs, and allows them to be read as a whole, rather than line-by-line.

            match = re.search("\d\d\d\d", clean)
            # a super basic regex looking for a 4-digit number.

            if match:
                the_year = match.group()
                # this search is not greedy and stops looking for 4-digit numbers after it finds one. With some exceptions, which will be corrected by hand, this will be the year of the event, because each text file begins with it's title, which contains the year in which it occured.
                if the_year in all_years:
                    all_years[the_year].append(clean)
                else:
                    all_years[the_year] = [clean]
                # This looks for a dictonary key for each year in the all_years dictionary, and adds the document's text if it finds one. If not, it creates a new key for that year, and adds a list containing the text as the value.

            else:
                uprint(str(f))
                #print the names of files that don't have a 4-digit number in them, for me to refer to manually and correct.
                continue


write = csv.writer(open('storybyyear.tsv', 'w'))

for key, value in all_years.items():
     write.writerow([key, " ", value])

# write all of this to a csv file, which I will then clean up some with openrefine.
