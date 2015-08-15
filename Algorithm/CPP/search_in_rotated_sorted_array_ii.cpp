# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
public:
	bool search(vector<int>& nums, int target)
	{
		int left = 0, right = nums.size()-1;
		while (left <= right)
		{
			int mid = (right - left) / 2 + left;
			if (nums[mid] == target) return true;
			if (nums[mid] < nums[right])
			{
				if (nums[mid] < target && target <= nums[right]) left = mid + 1;
				else right = mid - 1;

			}
			else if (nums[mid] > nums[right])
			{
				if (nums[left] <= target && target < nums[mid]) right = mid - 1;
				else left = mid + 1;
			}
			else
			{
				right -= 1;

			}
		}
		return false;
	}
};
int  main()
{
	Solution sol;
	vector<int> nums = { 4, 5, 6, 7, 8, 1, 2, 3,3 };
	int target =  8;
	//nums = { 5, 1, 3 };
	//target = 3;
	nums = { 3, 1 };
	target = 4;
	cout << sol.search(nums,target) << endl;
	cin.get();
	return 0;
}
