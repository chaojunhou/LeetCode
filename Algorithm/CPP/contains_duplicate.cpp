# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

class Solution {
public:
	bool containsDuplicate(vector<int>& nums) {
		unordered_map<int, int> dic;
		for (auto num : nums)
		{
			dic[num]++;
		}
		return dic.size() != nums.size();
	}
};
