# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	bool containsNearbyDuplicate(vector<int>& nums, int k) {
		unordered_map<int, int> myMap;
		int count = 0;
		for (int i = 0; i < nums.size();i++)
		{
			if (myMap.find(nums[i])==myMap.end())
			{
				myMap[nums[i]] = i;
			}
			else
			{
				if (i - myMap[nums[i]] <= k)
				{
					count++;
				}
				myMap[nums[i]] = i;
			}
		}
	
		return count == 1;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = {1,0,1,1};
	string s = "ccc";
	string t = "cc";
	cout << sol.containsNearbyDuplicate(nums,1);

	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
