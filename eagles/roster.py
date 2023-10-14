# create sql tables and insert data
import operator
file1 = open ('eagles_2023_off_roster.csv', 'r')
lines = file1.readlines()

file2 = open ('eagles_2023_off_roster_clean.csv', 'w')

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
    file2.write (output) 

file2. close
