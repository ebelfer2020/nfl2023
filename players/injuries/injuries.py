import pandas as pd
injuries_2023_url = 'https://www.espn.com/nfl/injuries'

injuries_2023_tables = pd.read_html(injuries_2023_url)

arz_injuries_2023 = injuries_2023_tables[0]
print ("Arizona Cardinals")
print (arz_injuries_2023)
arz_injuries_2023.to_csv("arz_injuries_2023.csv")

atl_injuries_2023 = injuries_2023_tables[1]
print ("Atlanta Falcons")
print (atl_injuries_2023)
atl_injuries_2023.to_csv("atl_injuries_2023.csv")

bal_injuries_2023 = injuries_2023_tables[2]
print ("Balitmore Ravens")
print (bal_injuries_2023)
bal_injuries_2023.to_csv("bal_injuries_2023.csv")


buf_injuries_2023 = injuries_2023_tables[3]
print("Bufflalo Bills")
print (buf_injuries_2023)
buf_injuries_2023.to_csv("buf_injuries_2023.csv")

car_injuries_2023 = injuries_2023_tables[4]
print("Carolina Panthers")
print (car_injuries_2023)
car_injuries_2023.to_csv("car_injuries_2023.csv")


chi_injuries_2023 = injuries_2023_tables[5]
print("Chicago Bears")
print (chi_injuries_2023)
chi_injuries_2023.to_csv("chi_injuries_2023.csv")


cin_injuries_2023 = injuries_2023_tables[6]
print("Cincinnati Benglas")
print (cin_injuries_2023)
cin_injuries_2023.to_csv("cin_injuries_2023.csv")

cle_injuries_2023 = injuries_2023_tables[7]
print("Cleveland Browns")
print (cle_injuries_2023)
cle_injuries_2023.to_csv("cle_injuries_2023.csv")


dal_injuries_2023 = injuries_2023_tables[8]
print("Dallas Cowboys")
print (dal_injuries_2023)
dal_injuries_2023.to_csv("dal_injuries_2023.csv")

den_injuries_2023 = injuries_2023_tables[9]
print("Denver Broncos")
print (den_injuries_2023)
den_injuries_2023.to_csv("den_injuries_2023.csv")

det_injuries_2023 = injuries_2023_tables[10]
print("Detroit Lions")
print (det_injuries_2023)
det_injuries_2023.to_csv("det_injuries_2023.csv")

gb_injuries_2023 = injuries_2023_tables[11]
print("Green Bay")
print (gb_injuries_2023)
gb_injuries_2023.to_csv("gb_injuries_2023.csv")

hou_injuries_2023 = injuries_2023_tables[12]
print("Houston Texans")
print (hou_injuries_2023)
hou_injuries_2023.to_csv("hou_injuries_2023.csv")


ind_injuries_2023 = injuries_2023_tables[13]
print("Indianapolis Colts")
print (ind_injuries_2023)
ind_injuries_2023.to_csv("ind_injuries_2023.csv")


jac_injuries_2023 = injuries_2023_tables[14]
print("Jacksonville Jaguars")
print (jac_injuries_2023)
jac_injuries_2023.to_csv("jac_injuries_2023.csv")


kc_injuries_2023 = injuries_2023_tables[15]
print("Kansas City Chiefs")
print (kc_injuries_2023)
kc_injuries_2023.to_csv("kc_injuries_2023.csv")


lv_injuries_2023 = injuries_2023_tables[16]
print("Las Vegas Raiders")
print (lv_injuries_2023)
lv_injuries_2023.to_csv("lv_injuries_2023.csv")

lac_injuries_2023 = injuries_2023_tables[17]
print("Los Angelese Chargers")
print (lac_injuries_2023)
lac_injuries_2023.to_csv("lac_injuries_2023.csv")


lar_injuries_2023 = injuries_2023_tables[18]
print("Los Angelese Rams")
print (lar_injuries_2023)
lar_injuries_2023.to_csv("lar_injuries_2023.csv")

mia_injuries_2023 = injuries_2023_tables[19]
print("Miami Dolphins")
print (mia_injuries_2023)
mia_injuries_2023.to_csv("mia_injuries_2023.csv")


min_injuries_2023 = injuries_2023_tables[20]
print("Minnesota Vikings")
print (min_injuries_2023)
min_injuries_2023.to_csv("min_injuries_2023.csv")


ne_injuries_2023 = injuries_2023_tables[21]
print("New England Patriots")
print (ne_injuries_2023)
ne_injuries_2023.to_csv("ne_injuries_2023.csv")

no_injuries_2023 = injuries_2023_tables[22]
print("New Orleans Saints")
print (no_injuries_2023)
no_injuries_2023.to_csv("no_injuries_2023.csv")


nyg_injuries_2023 = injuries_2023_tables[23]
print("New York Giants")
print (nyg_injuries_2023)
nyg_injuries_2023.to_csv("nyg_injuries_2023.csv")


nyj_injuries_2023 = injuries_2023_tables[24]
print("New York Jets")
print (nyj_injuries_2023)
nyj_injuries_2023.to_csv("nyj_injuries_2023.csv")


phi_injuries_2023 = injuries_2023_tables[25]
print("Philadelphia Eagles")
print (phi_injuries_2023)
phi_injuries_2023.to_csv("phi_injuries_2023.csv")


pit_injuries_2023 = injuries_2023_tables[26]
print("Pittsburgh Steelers")
print (pit_injuries_2023)
pit_injuries_2023.to_csv("pit_injuries_2023.csv")

sf_injuries_2023 = injuries_2023_tables[27]
print("San Francisco 49ers")
print (sf_injuries_2023)
sf_injuries_2023.to_csv("sf_injuries_2023.csv")

sea_injuries_2023 = injuries_2023_tables[28]
print("Seattle Seahawks")
print (sea_injuries_2023)
sea_injuries_2023.to_csv("sea_injuries_2023.csv")

tb_injuries_2023 = injuries_2023_tables[29]
print("Tampa Bay Buccaneers")
print (tb_injuries_2023)
tb_injuries_2023.to_csv("tb_injuries_2023.csv")

ten_injuries_2023 = injuries_2023_tables[30]
print("Tennessee Titans")
print (ten_injuries_2023)
ten_injuries_2023.to_csv("ten_injuries_2023.csv")

was_injuries_2023 = injuries_2023_tables[31]
print("Washington Commanders")
print (was_injuries_2023)
was_injuries_2023.to_csv("was_injuries_2023.csv")
