import pandas as pd
steelers_2023_url = 'https://www.espn.com/nfl/team/roster/_/name/pit/pittsburgh-steelers'

steelers_2023_tables = pd.read_html(steelers_2023_url)

steelers_2023_off_roster = steelers_2023_tables[0]
print ("Offense")
print(steelers_2023_off_roster)
steelers_2023_off_roster.to_csv("steelers_2023_off_roster.csv")


steelers_2023_def_roster = steelers_2023_tables[1]
print ("Defense")
print(steelers_2023_def_roster)
steelers_2023_def_roster.to_csv("steelers_2023_def_roster.csv")


steelers_2023_st_roster = steelers_2023_tables[2]
print ("Speical Teams")
print(steelers_2023_st_roster)
steelers_2023_st_roster.to_csv("steelers_2023_st_roster.csv")
