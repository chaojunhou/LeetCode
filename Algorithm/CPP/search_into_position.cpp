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
	int searchInsert(vector<int>& nums, int target) {
		int right = nums.size() - 1;
		int left = 0;
		while (left < right)
		{
			int mid = (right - left) / 2 + left;
			//if (nums[mid] == target) return mid;
			if (nums[mid] < target)
			{
				left = mid+1;
			}
			if (nums[mid] >= target)
			{
				right = mid;
			}
		}
		return (nums[left]>=target)?left:(left+1);

	}
};


int main()
{
	Solution sol;
	vector<int> nums = { 1, 3, 5, 6 };
	int target = 7;
	nums = { 1 };
	target = 1;
	cout << sol.searchInsert(nums, target) << endl;
	system("pause");
}


