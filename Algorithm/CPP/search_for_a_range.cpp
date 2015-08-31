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
	vector<int> searchRange(vector<int>& nums, int target) {
		int left = 0;
		int right = nums.size() - 1;
		vector<int> res(2,-1);
		while (left<=right)
		{
			int mid = (right - left) / 2 + left;
			if (nums[mid] == target) break;
			else if (nums[mid] < target) left = mid + 1;
			else right = mid - 1;
			
		}
		if (left > right) return res;
		while (nums[left] != target) left++;
		while (nums[right] != target) right--;
		if (left <= right)
		{
			res[0] = left;
			res[1] = right;
		}
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 5, 7, 7, 8, 8, 10 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };

	for(auto k:sol.searchRange(nums, k))cout<<k << endl;
	system("pause");
	return 0;
}
