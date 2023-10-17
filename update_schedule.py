# create bash script for weekly update of schedule with scorces

file1 = open ('sorted.txt', 'r')
lines = file1.readlines()

def run_python (team):
    statement = "python3 /home/ebelfer/nfl2023/" + team.strip('\n') + "/" + team.strip('\n') + "_2023_schedule.py\n"
    return statement


file2 = open ('update.sh', 'w')
file2.write("# /bin/bash")
file2.write('\n')

for line in lines:
   view_table_out = run_python(line)
   print (view_table_out)
   output = ''.join(view_table_out) 
   file2.write (output) 

file2. close
