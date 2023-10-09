import pandas as pd
import numpy as np
url = 'https://en.wikipedia.org/wiki/2023_Philadelphia_Eagles_season'


tables = pd.read_html(url)
schedule = tables[9]
print(schedule)
schedule.to_csv("eaglesschedule2023.csv")
