import pandas as pd
eagles_2023_url = 'https://en.wikipedia.org/wiki/2023_Philadelphia_Eagles_season'

eagles_2023_tables = pd.read_html(eagles_2023_url)
eagles_2023_schedule = eagles_2023_tables[9]
print(eagles_2023_schedule)
eagles_2023_schedule.to_csv("~/nfl2023/eagles/eagles_2023_schedule.csv")
