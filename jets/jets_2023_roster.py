import pandas as pd
jets_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/nyj/new-york-jets'

jets_2023_tables = pd.read_html(jets_2023_url)

jets_2023_off_roster = jets_2023_tables[0]
print ("Offense")
print(jets_2023_off_roster)
jets_2023_off_roster.to_csv("jets_2023_off_roster.csv")


jets_2023_def_roster = jets_2023_tables[1]
print ("Defense")
print(jets_2023_def_roster)
jets_2023_def_roster.to_csv("jets_2023_def_roster.csv")


jets_2023_st_roster = jets_2023_tables[2]
print ("Speical Teams")
print(jets_2023_st_roster)
jets_2023_st_roster.to_csv("jets_2023_st_roster.csv")
