# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	int maxSubArray(vector<int>& nums) {
		int summy = 0;
		int max_so_far = 0;
		int end_here = 0;
		for (int i = 0; i < nums.size(); ++i)
		{
			summy += nums[i];
			if (summy < 0)
				summy = 0;
			if (summy > max_so_far)
			{
				max_so_far = summy;
				end_here = i;
			}

		}
		if (max_so_far == 0)
			return *max_element(nums.begin(),nums.end());
		cout << end_here << endl;  // after get the end_here, we can iterate from the end_here to the first until the summy is max_so_far
		return max_so_far;

	}
};
int  main()
{
	Solution sol;
	vector<int> nums = {1,3,4,-3,9,2};
	//nums = { -1 };
	cout<<sol.maxSubArray(nums);
	cin.get();
	return 0;
}
