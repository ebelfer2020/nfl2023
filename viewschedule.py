# views sql tables

file1 = open ('sorted.txt', 'r')
lines = file1.readlines()

def view_table (team):
    view = "SELECT * FROM " + team.strip('\n') + "_2023_schedule;\n"
    return view


file2 = open ('view.sql', 'w')

for line in lines:
   view_table_out = view_table(line)
   print (view_table_out)
   output = ''.join(view_table_out) + "\n"
   file2.write (output) 

file2. close
