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
	int majorityElement(vector<int>& nums) {
		int res = nums[0];
		int count = 0;
		for (auto num : nums)
		{
			if (num == res) count++;
			else {
				count--;
				if (count < 0)
				{
					res = num;
					count = 1;
				}
			}
		}
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 3, 2, 3 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	cout << sol.majorityElement(nums) << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
