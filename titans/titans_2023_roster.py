import pandas as pd
titans_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/ten/tennessee-titans'

titans_2023_tables = pd.read_html(titans_2023_url)

titans_2023_off_roster = titans_2023_tables[0]
print ("Offense")
print(titans_2023_off_roster)
titans_2023_off_roster.to_csv("titans_2023_off_roster.csv")


titans_2023_def_roster = titans_2023_tables[1]
print ("Defense")
print(titans_2023_def_roster)
titans_2023_def_roster.to_csv("titans_2023_def_roster.csv")


titans_2023_st_roster = titans_2023_tables[2]
print ("Speical Teams")
print(titans_2023_st_roster)
titans_2023_st_roster.to_csv("titans_2023_st_roster.csv")
