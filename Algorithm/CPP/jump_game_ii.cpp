# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;



class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
		int total = 0;
		int sum = 0;
		int n = gas.size();
		int res=-1;
		for (int i = 0; i < n; i++)
		{
			sum += gas[i] - cost[i];
			if (sum < 0)
			{
				res = i;
				sum = 0;
			}
			total += gas[i] - cost[i];
		}
		if (total < 0) return -1;
		else return res+1;        
    }
};
