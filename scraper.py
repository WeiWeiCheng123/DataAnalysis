import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


good_read_book = pd.read_csv('books.csv', error_bad_lines = False)
genre = []

def scraper(isbn):
    web = 'https://www.goodreads.com/search?q=' + isbn
    response = requests.get(web)
    soup = BeautifulSoup(response.content.decode('big5', 'ignore'), "html.parser")
    cag = soup.find_all('a',{'class':'actionLinkLite bookPageGenreLink'}, limit=1)
    if len(cag):
        genre.append(cag[0].getText())
        #print(cag[0].getText())
    else:
        genre.append(None)
    

#counter = 0
for i in good_read_book['isbn']:
    #print(good_read_book.iloc[counter].title)
    scraper(i)
    #counter+=1

np.save('genre.npy',genre)