# What We Talk About When We Talk About Alien Encounters
This project, as a part of Doctoral Seminar LIS 3600: The Digital & The Humanities at the University of Pittsburgh's iSchool, explores the Western fascination with extra terrestrials, UFOs and alien encounters over the past 150 years. Drawing on early and pulp scifi, newspaper articles, government reports, and first-person encounters, this project aims to depict the history of our understanding of what an 'alien' is, and how disparate genres and narrative forms influence our cultural understanding of the ultimate 'Other'.

## Research Questions
- What are the prevailing terms, actions and themes that appear in stories about UFO encounters and alien abductions? How have they changed over time?
- In what ways has the history of SciFi literature influenced the way people describe their own encounters with extraterrestrials?
- What are the documents that UFO conspiracy theorists refer to when connecting the US government to UFOs, and how do they verify the legitimacy of these documents?


## 10/08/16:
### Resources collected:
#### SciFi
- Full text of "[The War of the Worlds](http://www.gutenberg.org/ebooks/36)", (1898) by H.G. Wells
- Full text of "[From the Earth to the Moon](http://www.gutenberg.org/ebooks/83)" (1865) and "Around the Moon" (1870) by Jules Verne (link to both books)
- Text of space-related stories from Astounding Stories from February - June 1930 ([Feb](http://www.gutenberg.org/ebooks/28617), [March](http://www.gutenberg.org/ebooks/29607), [April](http://www.gutenberg.org/ebooks/29390), [May](http://www.gutenberg.org/ebooks/29809), [June](http://www.gutenberg.org/ebooks/29848) )
  - Brigands of the Moon, by Ray Cummings
  - Into Space, by Sterner St. Paul
  - Spawn of the Stars, by Charles Willard Diffin
  - The Jovian Jest, by By Lilith Lorraine
  - Vandals of the Stars, by By A. T. Locke
- ["The Aliens"](http://www.gutenberg.org/ebooks/24104) (1959), by Murray Leinster

#### Roswell Incident
- [United Press Roswell Telex Report](http://roswellproof.homestead.com/United_Press_Telexes.html), July 8, 1947
- [Associated Press Roswell Reports](http://roswellproof.homestead.com/AP_Earliest_July8.html) [(2)](http://roswellproof.homestead.com/LA_HeraldExpress_July8.html), July 8, 1947
- [Forth Worth Star-Telegram "New Mexico Rancher's 'Flying Disk' Proves to Be Weather Balloon-Kite"](http://roswellproof.homestead.com/FortWorthST_July9.html) July 9, 1947
- [Roswell Daily Record "Harassed Rancher who Located 'Saucer' Sorry He Told About it"](http://roswellproof.homestead.com/brazel_interview.html) Roswell Daily Record, July 9, 1947
- [Robertson Panel proceedings, contained in the Durant Report](http://www.cufon.org/cufon/robert.htm) (1953)

#### Encounter Stories
- 402 alien/UFO encounter stories from http://ufocasebook.com (1878-2012)
- 12 alien abduction stories from the Minnesota MUFON chapter http://mnmufon.org (1969-1998)

### Methods and Tools
The resources I have collected so far have come via web searches and browsing through UFO-related websites, which I have scraped with the mnmufon_scrape.py and ufocasebook.py scripts in this repository, and cleaned with htmlstrip.py. These websites, additionally, have been crawled and documented with Archive.org's Wayback Machine, to create a reflection of their structure and contents on the days that I scraped them. The SciFi texts are all freely available through Project Gutenberg, and the transcriptions of Roswell news stories come from conspiracy-related websites.

While it may seem that texts, such as the Roswell news stories, and the Robertson Panel report that are maintained and transcribed by the same UFO conspiracy sites as the UFO encounter stories I have collected, I would argue that the accuracy or even veracity of these texts are largely irrelevant, given that their audience believes in their accuracy, and they serve as foundational documents for the UFO conspiracy, regardless of whether they are 100% historically accurate.

### Next Steps
As this research moves into analysis, all of the texts will be examined using a variety of tools and methods, including word-frequency analysis (using Voyant), topic clustering (using Gephi), and potentially sentiment analysis (using IBM Watson's Personality Insights). Sentiment analysis, especially with freely available tools can be tricky, since the "baseline" dictionary to which texts are compared often assumes contemporary vocabulary, and a certain style of rhetoric.

Before conducting this analysis, however, the UFO incident stories need to be further cleaned and cataloged. Rather than reading and evaluating each narrative individually, my aim is to look at larger themes and trends over time. The next step in this process is to sort the ufocasebook.com incidents into categories by year/decade/other time spans, so that their texts can be better analyzed as a whole. This will be done with a python script that uses regular expressions to find the date within the document (located at a predictable place within the text), and sorts them into the appropriate lists, which will then be written as .csv files.

After running all of the available resources through the various tools, listed above, I will evaluate how best to interpret, describe and present my findings. My preliminary idea is a timeline, since these documents span
nearly 150 years worth of history. Tools such as TimelineJS and Tableau Public would be useful for creating such visualizations. Additionally, if the cluster analysis with Gephi proves a rich vein, further network analysis may be justified.

### Further Reading & Resources
Bader, C. D., Mencken, F. C. C., & Baker, J. O. (2011). _Paranormal America : Ghost Encounters, UFO Sightings, Bigfoot Hunts, and Other Curiosities in Religion and Culture_. New York, US: NYU Press. Retrieved from http://www.ebrary.com.pitt.idm.oclc.org

Barkun, M. (2013). _A culture of conspiracy: Apocalyptic visions in contemporary America_ (Vol. 15). Univ of California Press.

Card, Stuart K, Jock D Mackinlay, and Ben Shneiderman. _Readings in Information Visualization: Using Vision to Think._ Morgan Kaufmann, 1999.

Gepper, A. T. (2012). "Extraterrestrial encounters: UFOs, science and the quest for transcendence, 1947-1972." _History & Technology_, 28(3), 335-362. doi:10.1080/07341512.2012.723340

Lambiotte, Renaud, Jean-Charles Delvenne, and Mauricio Barahona. _“Laplacian Dynamics and Multiscale Modular Structure in Networks.”_ (2009) http://arxiv.org/abs/0812.1770.

Lin, Y. (2012). "Transdisciplinarity and digital humanities: Lessons learned from developing text-mining tools for textual analysis",   _Understanding Digital Humanities_, Palgrave Macmillan, Houndmills, Basingstoke, pp. 295-314.

#### Tools
- Gephi: http://gephi.org
- IBM Watson Personality Insights: http://www.ibm.com/watson/developercloud/personality-insights.html
- Tableau Public: http://public.tableau.com
- TimelineJS: http://timeline.knightlab.com
- Voyant: http://voyant-tools.org/
