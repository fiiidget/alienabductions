from bs4 import BeautifulSoup
import requests
import sys
import csv

link_list = []

url = ('http://www.ufocasebook.com/casefiles.html')

ufo_page = requests.get(url)

if ufo_page.status_code != 200:
    print ("there was an error with", url)


page_html = ufo_page.text

page_html = page_html.encode('ascii', 'ignore').decode('ascii')

soup = BeautifulSoup(page_html, "html.parser")

story_table = soup.find_all("td", attrs = {"style" : "border: 0px solid rgb(116, 116, 116);"})

for table_row in story_table:
    a_row = table_row.find_all("table", attrs = {"width" : "98%"})

    for row in a_row:
        a_link = row.find_all("a")

        for the_link in a_link:
            link = the_link["href"]

            link_list.append(link)


print(a_row)
#
# with open('mnmufon.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(text_lists)
