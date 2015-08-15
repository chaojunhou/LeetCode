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
	int findMin(vector<int>& nums) 
	{
		int right = nums.size() - 1;
		int left = 0;
		while (left < right && nums[left] > nums[right])
		{
			int mid = (right - left) / 2 + left;
			if (nums[mid] < nums[right]) right = mid ;
			else left = mid+1;
			//cout << left << " " << right << " right" << endl;
		}
		return nums[left];
	}
};


int main()
{
	Solution sol;
	vector<int> nums = { 4 ,5, 6, 7, 0, 1, 2 ,3
	};
	cout << sol.findMin(nums) << endl;
	system("pause");
}
