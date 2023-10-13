import pandas as pd

#opening spreads
week1_2023_url = 'https://www.rotowire.com/betting/nfl/odds/week-1'
week1_2023_tables = pd.read_html(week1_2023_url)
week1 = week1_2023_tables[0]
print ("Week 1 opening spreads")
print(week1)
week1.to_csv("week1_spreads.csv")


week2_2023_url = 'https://www.rotowire.com/betting/nfl/odds/week-2'
week2_2023_tables = pd.read_html(week2_2023_url)
week2 = week2_2023_tables[0]
print ("Week 2 opening spreads")
print (week2)
week2.to_csv("week2_spreads.csv")


week3_2023_url = 'https://www.rotowire.com/betting/nfl/odds/week-3'
week3_2023_tables = pd.read_html(week3_2023_url)
week3 = week3_2023_tables[0]
print ("Week 3 opening spreads")
print (week3)
week3.to_csv("week3_spreads.csv")

week4_2023_url = 'https://www.rotowire.com/betting/nfl/odds/week-4'
week4_2023_tables = pd.read_html(week4_2023_url)
week4 = week4_2023_tables[0]
print ("Week 4 opening spreads")
print (week4)
week4.to_csv("week4_spreads.csv")

week5_2023_url = 'https://www.rotowire.com/betting/nfl/odds/week-5'
week5_2023_tables = pd.read_html(week5_2023_url)
week5 = week5_2023_tables[0]
print ("Week 5 opening spreads")
print (week5)
week5.to_csv("week5_spreads.csv")


week6_2023_url = 'https://www.rotowire.com/betting/nfl/odds/week-6'
week6_2023_tables = pd.read_html(week6_2023_url)
week6 = week6_2023_tables[0]
print ("Week 6 opening spreads")
print (week6)
week5.to_csv("week6_spreads.csv")
