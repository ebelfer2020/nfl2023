import pandas as pd
rushing_2023_url = 'https://www.pro-football-reference.com/years/2023/rushing.htm'

rushing_2023_tables = pd.read_html(rushing_2023_url)
rushing_2023 = rushing_2023_tables[0]
print(rushing_2023)
rushing_2023.to_csv("rushing_2023.csv")
