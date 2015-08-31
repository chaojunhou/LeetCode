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
	int removeDuplicates(vector<int>& nums) {


		int n = nums.size();
		if (n < 2) return nums.size();
		int slow = 0, fast = 1;
		while (fast < n)
		{
			if (nums[slow] != nums[fast])
			{
				nums[++slow] = nums[fast++];
			}
			else
			{
				++fast;
			}
		}
		return slow + 1;

	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1,1,2,3,3 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	cout << sol.removeDuplicates(nums) << endl;
	for (auto k :nums )cout << k << endl;
	system("pause");
	return 0;
}

