from bs4 import BeautifulSoup
import requests
import sys
import csv

link_list = []

with open("RP_subURLs.csv") as f:
    for subpage in map(str.strip,f):      # Number of pages plus one
        url = "http://www.roswellproof.homestead.com/{}".format(subpage)

        ufo_page = requests.get(url)

        if ufo_page.status_code != 200:
            print ("there was an error with", url)


        page_html = ufo_page.text

        page_html = page_html.encode('ascii', 'ignore').decode('ascii')

        soup = BeautifulSoup(page_html, "html.parser")
        #
        page_links = soup.find_all("a")
        # # story_table = soup.find_all("td", attrs = {"style" : "border: 0px solid rgb(116, 116, 116);"})
        # #
        # # for table_row in story_table:
        # #     a_row = table_row.find_all("table", attrs = {"width" : "98%"})
        # #
        # #     for row in a_row:
        # #         a_link = row.find_all("a")
        # #
        # for the_link in page_links:
        #     link = the_link["href"]
        # #
        #     link_list.append(link)
#CURRENTLY: (NOON 6/30) IS NOT WRITING TO A LIST, JUST LOOPING THROUGH AND LOOKING.
#NEED TO GET JUST THE HREF, WITHOUT AN IDIOT ERROR.
#WHY

#
print(page_links)
# #
# # with open('mnmufon.csv', 'w', newline='') as f:
# #     writer = csv.writer(f)
# #     writer.writerow(text_lists)
