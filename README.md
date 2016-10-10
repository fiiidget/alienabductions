# alienabductions
This project, as a part of Doctoral Seminar LIS 3600: The Digital & The Humanities at the University of Pittsburgh's iSchool, explores the Western fascination with extra terrestrials, UFOs and alien encounters over the past 150 years. Drawing on early and pulp scifi, newspaper articles, government reports, and first-person encounters, this project aims to depict the history of our understanding of what an 'alien' is, and how disparate genres and narrative forms influence our cultural understanding of the ultimate 'Other'.

## Research Questions

## 10/08/16:
### Resources collected:
#### SciFi
- Full text of "The War of the Worlds", (1898) by H.G. Wells
- Full text of "From the Earth to the Moon" (1865) and "Around the Moon" (1870) by Jules Verne
- Text of space-related stories from Astounding Stories from January - June 1930
  - Brigands of the Moon, by Ray Cummings
  - Into Space, by Sterner St. Paul
  - Spawn of the Stars, by Charles Willard Diffin
  - The Jovian Jest, by By Lilith Lorraine
  - Vandals of the Stars, by By A. T. Locke
- "The Aliens" (1959), by Murray Leinster

#### Roswell Incident
- United Press Roswell Telex Report, July 8, 1947
- Associated Press Roswell Reports (2), July 8, 1947
- Forth Worth Star-Telegram "New Mexico Rancher's 'Flying Disk' Proves to Be Weather Balloon-Kite"
- Roswell Daily Record "Harassed Rancher who Located 'Saucer' Sorry He Told About it"
- Robertson Panel proceedings, contained in the Durant Report (1953)

#### Encounter Stories
- 402 alien/UFO encounter stories from http://ufocasebook.com (1878-2012)
- 12 alien abduction stories from the Minnesota MUFON chapter http://mnmufon.org (1969-1998)

### Methods and Tools
The resources I have collected so far have come via web searches and browsing through UFO-related websites, which I have scraped with the mnmufon_scrape.py and ufocasebook.py scripts in this repository, and cleaned with htmlstrip.py. These websites, additionally, have been crawled and documented with Archive.org's Wayback Machine, to create a reflection of their structure and contents on the days that I scraped them. The SciFi texts are all freely available through Project Gutenberg, and the transcriptions of Roswell news stories come from conspiracy-related websites.

While it may seem that texts, such as the Roswell news stories, and the Robertson Panel report that are maintained and transcribed by the same UFO conspiracy sites as the UFO encounter stories I have collected, I would argue that the accuracy or even veracity of these texts are largely irrelevant, given that their audience believes in their accuracy, and they serve as foundational documents for the UFO conspiracy, regardless of whether they are 100% historically accurate.

### Next Steps
As this research moves into analysis, all of the texts will be examined using a variety of tools and methods, including word-frequency analysis (using Voyant), topic clustering (using Gephi), and potentially sentiment analysis (using IBM Watson's Personality Insights). Sentiment analysis, especially with freely available tools can be tricky, since the "baseline" dictionary to which texts are compared often assumes contemporary vocabulary, and a certain style of rhetoric.

Before conducting this analysis, however, the UFO incident stories need to be further cleaned and cataloged. Rather than reading and evaluating each narrative individually, my aim is to look at larger themes and trends over time. The next step in this process is to sort the ufocasebook.com incidents into categories by year/decade/other time spans, so that their texts can be better analyzed as a whole.

### Further Reading & Resources
