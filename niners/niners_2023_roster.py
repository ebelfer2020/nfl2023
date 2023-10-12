import pandas as pd
niners_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/sf/san-francisco-49ers'

niners_2023_tables = pd.read_html(niners_2023_url)

niners_2023_off_roster = niners_2023_tables[0]
print ("Offense")
print(niners_2023_off_roster)
niners_2023_off_roster.to_csv("niners_2023_off_roster.csv")


niners_2023_def_roster = niners_2023_tables[1]
print ("Defense")
print(niners_2023_def_roster)
niners_2023_def_roster.to_csv("niners_2023_def_roster.csv")


niners_2023_st_roster = niners_2023_tables[2]
print ("Speical Teams")
print(niners_2023_st_roster)
niners_2023_st_roster.to_csv("niners_2023_st_roster.csv")
