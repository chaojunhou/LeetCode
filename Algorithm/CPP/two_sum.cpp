# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
# include <vector>
# include <unordered_map>
# include <map>
using namespace std;

class Solution {
public:
	vector<int> twoSum1(vector<int>& nums, int target) 
	{
	unordered_map<int, int> hash;
	vector<int> res;
	for (auto i = 0; i < nums.size(); ++i)
	{
		if (hash.find(nums[i]) == hash.end())
			hash[nums[i]] = i;
	}

	for (int i = nums.size() - 1; i > -1; --i)
	{
		if (hash.find(target - nums[i]) != hash.end())
		{
			if ((i) != (hash[target - nums[i]]))
			{
				res.push_back(hash[target - nums[i]] + 1);
				res.push_back(i + 1);
				return res;
			}
		}
	}
	}

	vector<int> twoSum ( vector<int>& nums, int target )
	{
		unordered_map<int, int> dic;
		vector <int> res;
		for (auto i = 0; i < nums.size(); ++i)
		{
			if (dic.find(target - nums[i]) != dic.end())
			{
				res.push_back(dic[target - nums[i]] + 1);
				res.push_back(i + 1);
				return res;
			}
			dic[nums[i]] = i;
		}
	}
};


int main()
{

	Solution sol;
	vector<int> numbers = { 2, 7, 11, 15 };
	auto target = 9;
	for (auto s : sol.twoSum(numbers, target))
		cout << s << " ";
	cout << endl;
	cin.get();
	return 0;
}
