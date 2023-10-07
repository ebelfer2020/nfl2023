from bs4 import BeautifulSoup
import requests
import pandas as pd
import io


url = 'https://en.wikipedia.org/wiki/2023_Philadelphia_Eagles_season'
source = requests.get(url).text

soup = BeautifulSoup (source, 'lxml')



tables = soup.find_all('table', class_ ='wikitable')
for x in tables:
  df = pd.read_html(str(x))  
  print (df)
