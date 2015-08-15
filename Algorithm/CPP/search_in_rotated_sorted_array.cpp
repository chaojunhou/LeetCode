# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	int search(vector<int>& nums, int target) {
		int left = 0, right = nums.size()-1;
		while (left <= right)
		{
			int mid = (right - left) / 2 + left;
			//cout << "left=" << left << " right=" << right <<" mid = "<<mid<< endl;
			if (nums[mid] == target) return mid;
			if (nums[mid]<nums[right] )  // compare the middle element with the right or the left not with the target
			{
				if (nums[mid] < target && target <= nums[right]) left = mid + 1;
				else right = mid - 1;
			}
			else
			{
				if (nums[left] <= target && target < nums[mid] ) right = mid - 1;
				else left = mid + 1;
			}
		}
		return -1;

	}
};
int  main()
{
	Solution sol;
	vector<int> nums = { 4, 5, 6, 7, 8, 1, 2, 3 };
	int target =  8;
	//nums = { 5, 1, 3 };
	//target = 3;
	cout << sol.search(nums,target) << endl;
	cin.get();
	return 0;
}
