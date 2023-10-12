import pandas as pd
texans_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/hou/houston-texans'

texans_2023_tables = pd.read_html(texans_2023_url)

texans_2023_off_roster = texans_2023_tables[0]
print ("Offense")
print(texans_2023_off_roster)
texans_2023_off_roster.to_csv("texans_2023_off_roster.csv")


texans_2023_def_roster = texans_2023_tables[1]
print ("Defense")
print(texans_2023_def_roster)
texans_2023_def_roster.to_csv("texans_2023_def_roster.csv")


texans_2023_st_roster = texans_2023_tables[2]
print ("Speical Teams")
print(texans_2023_st_roster)
texans_2023_st_roster.to_csv("texans_2023_st_roster.csv")
