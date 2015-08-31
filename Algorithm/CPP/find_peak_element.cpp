# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int findPeakElement(vector<int>& nums) {
		int n = nums.size();
		return find(nums, 0, n - 1);
	}
	int find(vector<int>& nums, int left, int right)
	{
		int mid = (right - left) / 2 + left;
		if ((mid == nums.size()-1 || nums[mid] > nums[mid + 1]) && (mid==0 || nums[mid] > nums[mid - 1])) return mid;
		else if (mid > 0 && nums[mid] < nums[mid - 1]) return find(nums, left , mid-1);
		else return find(nums, mid+1, right);
	}
};

int main()
{
	Solution sol;
	vector<int> nums = {1,2,3,1};

	cout<<sol.findPeakElement(nums);

	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}


