import pandas as pd
fantasy_2023_url = 'https://www.pro-football-reference.com/years/2023/fantasy.htm'

fantasy_2023_tables = pd.read_html(fantasy_2023_url)
fantasy_2023 = fantasy_2023_tables[0]
print(fantasy_2023)
fantasy_2023.to_csv("fantasy_2023.csv")
