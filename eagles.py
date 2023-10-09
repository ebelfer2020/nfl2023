import pandas as pd
import numpy as np
url = 'https://en.wikipedia.org/wiki/2023_Philadelphia_Eagles_season'


schedule =pd.read_html(url)
print (schedule[9])
