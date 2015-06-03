#！bin/awk -f
# Solution 1
awk '{
    for (i=1; i<=NF; i++)
    	if (NR == 1){
    		words[i] = $i; 
    	}else{
    		words[i] = words[i] " " $i;
    	}
}
END {
    for (i=1; words[i]!= " ";i++)
         print words[i]
}' file.txt

# Solution 2
awk '{
  for (i=1; i<=NF; i++)
  {
  	matrix[NR,i] = $i;
  }

END{
	for (i=1; i<=NF; i++)
	{
		line = matrix[1,i]
		for (j =2; j<NR; j++)
		{
			line = line " " matrix[j,i]
		}
		print line;
	}
}

}' file.txt