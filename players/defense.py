import pandas as pd
defense_2023_url = 'https://www.pro-football-reference.com/years/2023/defense.htm'

defense_2023_tables = pd.read_html(defense_2023_url)
defense_2023 = defense_2023_tables[0]
print(defense_2023)
defense_2023.to_csv("defense_2023.csv")
