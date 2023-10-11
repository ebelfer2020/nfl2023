import pandas as pd
passing_2023_url = 'https://www.pro-football-reference.com/years/2023/passing.htm'

passing_2023_tables = pd.read_html(passing_2023_url)
passing_2023 = passing_2023_tables[0]
print(passing_2023)
passing_2023.to_csv("passing_2023.csv")
