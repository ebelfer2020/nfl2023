import pandas as pd
ravens_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/bal/baltimore-ravens'

ravens_2023_tables = pd.read_html(ravens_2023_url)

ravens_2023_off_roster = ravens_2023_tables[0]
print ("Offense")
print(ravens_2023_off_roster)
ravens_2023_off_roster.to_csv("ravens_2023_off_roster.csv")


ravens_2023_def_roster = ravens_2023_tables[1]
print ("Defense")
print(ravens_2023_def_roster)
ravens_2023_def_roster.to_csv("ravens_2023_def_roster.csv")


ravens_2023_st_roster = ravens_2023_tables[2]
print ("Speical Teams")
print(ravens_2023_st_roster)
ravens_2023_st_roster.to_csv("ravens_2023_st_roster.csv")
