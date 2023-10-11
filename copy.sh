#!/bin/bash
input="sorted.txt"

while IFS= read -r line
do
  echo "copy to ${line}"
  cp eagles_2023_roster.py ${line}/"${line}_2023_roster.py"
done < "$input"
