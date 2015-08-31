# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

class Solution {
public:
	bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
		if (k < 1 || t < 0)return false;
		unordered_map<int, int> dic;
		int key;
		for (int i = 0; i < nums.size(); i++)
		{
		
			if (t>1)
			{
				key = nums[i] / t;
				if (nums[i] < 0 && nums[i]%t) key--;
			}
			else key = nums[i];
			if ( dic.find(key) != dic.end() ||
				(dic.find(key - 1) != dic.end() && abs(dic[key - 1] - nums[i]) <= t) ||
				(dic.find(key + 1) != dic.end() && abs(dic[key + 1] - nums[i]) <= t) )
				return true;
			if (dic.size() == k) dic.erase(dic.begin());
			dic[key] = nums[i];
		}
		return false;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 2, 0, -2, 2  };
	cout << sol.containsNearbyAlmostDuplicate(nums, 2, 1);

	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}

