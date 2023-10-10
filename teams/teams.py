import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml
import csv
import re

url = 'https://www.pro-football-reference.com/years/2023/'
#df = pd.read_html(url)
#print (df)

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
table = soup.find('div', id="all_team_stats")

generator_expr = (str(element) for element in table)
separator = ' '
result_string = separator.join(generator_expr)

pattern = re.compile('<.*?>')
table = re.sub(pattern, ' ', result_string)
print (table)


