import pandas as pd
receiving_2023_url = 'https://www.pro-football-reference.com/years/2023/receiving.htm'

receiving_2023_tables = pd.read_html(receiving_2023_url)
receiving_2023 = receiving_2023_tables[0]
print(receiving_2023)
receiving_2023.to_csv("receiving_2023.csv")
