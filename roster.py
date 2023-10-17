# create sql tables and insert data
import operator

path  = "/home/ebelfer/nfl2023/"
team_file = open ( path + 'sorted.txt', 'r')
teams = team_file.readlines()

def clean_csv (lines):
  for line in lines:
    line_list = list(line.split(","))
    print (line_list)
    name_number =line_list[2]
    print (name_number)
    length = len(name_number)
    number = operator.getitem(name_number, slice(length-2,length))
    name = name_number[:-2]
    if not number.isnumeric():
      number = operator.getitem(name_number, slice(length-1,length))
      name = name_number[:-1]    
    print (name)
    print (number)
    index = line_list[0]
    position = line_list[3]
    age = line_list[4]
    height = (line_list[5][:-2])
    years = line_list[7]
    college = line_list[8]
    print (college)
    new_line =  [index, name, number, position, age, height, years, college]
    print (new_line) 
    output = ','.join(new_line) 
    file_output.write (output) 
    file_output.close

for team in teams:
  team = team.strip('\n')
  path = "/home/ebelfer/nfl2023/" + team + "/"
  file_output = open (path + team + '_2023_roster_clean.csv', 'w')
  file_off = open (path + team + '_2023_off_roster.csv', 'r')
  lines_off = file_off.readlines()
  file_def = open (path + team + '_2023_def_roster.csv', 'r')
  lines_def = file_def.readlines() 
  file_st = open (path + team + '_2023_st_roster.csv', 'r')
  lines_st = file_st.readlines()
  file_output = open (path + team + '_2023_roster_clean.csv', 'a')
  clean_csv(lines_off)
  clean_csv(lines_def)
  clean_csv(lines_st)
  file_output.close()
