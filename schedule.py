# create sql tables and insert data

file1 = open ('sorted.txt', 'r')
lines = file1.readlines()

def create_table (team):
  table = "CREATE TABLE " + team.strip('\n') + "_2023_schedule\n" \
           "id INTEGER,\n" \
           "week INTEGER,\n" \
           "date VARCHAR(15),\n" \
           "time VARCHAR(10),\n" \
           "opponent VARCHAR(30),\n" \
           "result VARCHAR (15),\n"\
           "recond VARCHAR (7),\n" \
           "venue  VARCHAR (30),\n" \
           "network VARCHAR(15), \n" \
           "recap VARCHAR(5), \n" \
           "PRIMARY KEY (id));"
  return table

def load_data (team):
  data = "LOAD DATA LOCAL INFILE ' ~/nfl2023/" + team.strip('\n') + "/" +team.strip('\n') + "_2023_schedule.csv'\n" \
           "INTO TABLE " + team.strip('\n') + "_2023_schedule\n" \
           "FIELDS TERMINATED BY ','\n" \
           "IGNORE 1 ROWS;"
  return data

file2 = open ('schedule.sql', 'w')

for line in lines:
   mtable = create_table(line)
   print (mtable)
   print ()
   load_data_out = load_data(line)
   print (load_data_out)
   print ()
   output = ' '.join(mtable) + "\n" + ' '.join(load_data_out) + "\n"
   file2.write (output) 

file2. close
