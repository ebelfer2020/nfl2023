# sorts nfl names

file1 = open ('names.txt', 'r')
lines = file1.readlines()
sort_teams = sorted(lines)
print (sort_teams)

file2 = open ('sorted.txt', 'w')
file2.writelines(sort_teams)
file2. close
