#I Want to Be Believed: Content and Structure as Value Propositions in Ufology Websites

##Introduction
While humans have reported seeing strange objects in the skies for as long as we have been documenting our experiences, the popularity and public fascination with these encounters has ebbed and flowed over the course of history. Since the industrial revolution, the possibility that creatures from other planets may have technologies similar or more advanced than our own has been a recurrent narrative in popular media (Jacobs 1973). Growing out of this fascination, especially after the widely-publicized “Roswell Incident” in 1947,  and in subsequent years, under the shadow of the USSR in the heart of the Cold War, groups dedicated to investigating UFO phenomena have emerged, spending their time and labor in an area that they believe is underrepresented in traditional scholarship (Denzler 2001, Wortman 2004). This project looks particularly at the evolution of these groups since the emergence of the internet, within the context of access to resources and the subjective nature of ‘acceptable’ resources and rhetoric, using documents transcribed into plain text and posted onto Ufology websites.

This project focuses on two websites, http://ufocasebook.com and http://roswelltruth.homestead.com. These sites were chosen because they are run by individuals, rather than as official branches of Ufology groups, and for their longevity (online since 2001, possibly earlier).

##Process
From these sites, documents falling into two categories were collected: UFO encounter narratives (400 individual stories, ~219,000 words), and supporting government/media reports (5 news reports, and the text of the Robertson Panel Report, ~11,000 words). Content analysis via word-frequency analysis and topic modelling were done on these two corpora using Voyant and MALLET, respectively.

Analyses on these corpora show themes of physical location and the movement of objects within the UFO encounter stories, whereas the government/media reports focus on reactions and explanations to previously observed phenomena. These sites collect different types of documentation, under the same umbrella of “Ufology”, using much of the same vocabulary, such as “sighting,” “report” and the crucial “ufo.”


##Contained Here
- Python scripts to scrape, clean and sort text from http://ufocasebook.com
- Python scripts to scrape and clean text from http://mnmufon.org (not used)

###Collected Data
- 400 UFO Encounter Stories, from http://ufocasebook.com
- Text of the Robertson Panel Report, from http://roswellproof.com
- Text of news reports from the 1947 Roswell Incident, from http://roswellproof.com

###For each of the above texts:
- Term frequency data, from Voyant (http://voyant-tools.org)
- Image files of term frequency, from Voyant, and Tableau Public (https://public.tableau.com/profile/s.e.hackney#!/vizhome/UFOEncounters/Dashboard1)
- .mallet files
- Topic key files (5, 10, 15, 20 & 25 topics) from MALLET (http://mallet.cs.umass.edu)

###Additional Resources
Also contained in this repository are the remnants of previous iterations of this projects, and explorations into other datasets. These include:
- Text from Sci Fi novels and short stories, 1865-1959, via http://projectgutenberg.org (not used)
- JSON files of sentiment analysis from IBM Watson Personality Insights (http://www.ibm.com/watson/developercloud/personality-insights.html)


## Further Reading & Resources
Bader, C. D., Mencken, F. C. C., & Baker, J. O. (2011). _Paranormal America : Ghost Encounters, UFO Sightings, Bigfoot Hunts, and Other Curiosities in Religion and Culture_. New York, US: NYU Press. Retrieved from http://www.ebrary.com.pitt.idm.oclc.org

Barkun, M. (2013). _A culture of conspiracy: Apocalyptic visions in contemporary America_ (Vol. 15). Univ of California Press.

Card, Stuart K, Jock D Mackinlay, and Ben Shneiderman. _Readings in Information Visualization: Using Vision to Think._ Morgan Kaufmann, 1999.

Denzler, Brenda. *The Lure of the Edge: Scientific Passions, Religious Beliefs, and the Pursuit of UFOs*. Univ of California Press, 2001.

Gepper, A. T. (2012). "Extraterrestrial encounters: UFOs, science and the quest for transcendence, 1947-1972." _History & Technology_, 28(3), 335-362. doi:10.1080/07341512.2012.723340

Jacobs, David Michael. *The controversy over unidentified flying objects in America: 1896-1973*. University of Wisconsin--Madison, 1973.

Keyhoe, Donald Edward. *Flying saucers from outer space*. Holt, 1953.

Lambiotte, Renaud, Jean-Charles Delvenne, and Mauricio Barahona. _“Laplacian Dynamics and Multiscale Modular Structure in Networks.”_ (2009) http://arxiv.org/abs/0812.1770.

Lin, Y. (2012). "Transdisciplinarity and digital humanities: Lessons learned from developing text-mining tools for textual analysis",   _Understanding Digital Humanities_, Palgrave Macmillan, Houndmills, Basingstoke, pp. 295-314.

Wortman, Anna. "The Roswell Myth in the FBI Files: Aliens, UFOs, and the Cold War." *Polish Journal for American Studies*, Vol. 1, pp. 181-190.  Wydawnictwo Naukowe UAM, Poznan, 2004


## Tools
- IBM Watson Personality Insights: http://www.ibm.com/watson/developercloud/personality-insights.html
- MALLET http://mallet.cs.umass.edu
- Tableau Public: http://public.tableau.com
- Voyant: http://voyant-tools.org/
