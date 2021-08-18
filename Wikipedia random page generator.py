import bs4
import requests
import webbrowser
import time
url = "https://en.wikipedia.org/wiki/Special:Random"
branch = requests.get(url)
soup = bs4.BeautifulSoup(branch.content, "html.parser")
title = soup.find(class_="firstHeading").text

t=0
#n = input(f'{title} \n Do you want to view this? If not, reload (Y/N): ')
def yes():
    url_title = (title.lower().replace(' ', '_'))
    url_link = 'https://en.wikipedia.org/wiki/{}'.format(url_title)
    if soup.find(class_="plainlinks").text == " to check for alternative titles or spellings.":
        return (soup.find(class_="external text").text)
    elif soup.find(class_="infobox").text == None:
        return None
    elif soup.find(class_="plainlinks").text != "to check for alternative titles or spellings.":
        return url_link
print(yes())
