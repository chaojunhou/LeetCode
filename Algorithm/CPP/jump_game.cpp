# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	bool canJump(vector<int>& nums) {
		int n = nums.size();
		int reach = 0;
		for (int i = 0; i < n; i++)
			if (i<=reach) reach = max(reach, nums[i] + i);
		return (reach>=(n-1));
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 3,2,1,0,4 };
	nums = { 0 };
	 //nums = {2,5,0,0};
	cout << sol.canJump(nums) << endl;
	system("pause");
	return 0;
}

