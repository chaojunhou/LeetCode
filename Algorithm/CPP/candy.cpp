# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
# include <algorithm>
# include <time.h>
# include<random>
# include <queue>
#include <stdint.h>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
		int n = ratings.size();
		vector<int> nums(n,1);
		for (int i = 1; i < n; i++)
			if (ratings[i]>ratings[i - 1]) nums[i] = nums[i - 1] + 1;
		for (int i = n - 2; i >= 0; i--)
			if (ratings[i] > ratings[i + 1] && nums[i + 1] >= nums[i])
				nums[i] = nums[i + 1] + 1;
		int sum=0;
		for (int i = 0; i < n; i++)
		{
			sum += nums[i];
		}
		return sum;        
    }
};
