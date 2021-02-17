from bs4 import BeautifulSoup
from Bible import Bible
import requests
import urllib
import os
import string

class Book:
    def getInfo(self, url, abbr):
        ## Get Chapter
        chapter = ''.join(i for i in url[-3:] if i.isdigit())

        ## Access web site
        url = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'}) 
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')

        ## Get verses Text
        verseBody = soup.find('article').find('div').find('div')
        verseRaw = verseBody.find_all('p')

        try:
            copyRight = verseBody.find('p', attrs={"class":"MuiTypography-body2"})
        except:
            copyRight = None

        if copyRight:
            verseRaw.pop()

        for i in range(0, len(verseRaw)):
            unwantedTag = verseRaw[i].find('sup')
            unwantedTag.extract()

        verse = []
        for i in range(0, len(verseRaw)):
            single_quote = "'"
            double_quote = '"'
            verse.append(verseRaw[i].text.lstrip().replace(double_quote, single_quote))
        
        return verse