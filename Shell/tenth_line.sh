# Solution 1
awk 'NR == 10' file.txt
# Solution 2
tail -n+10 file.txt | head -1 
