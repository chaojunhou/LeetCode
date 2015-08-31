# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	void nextPermutation(vector<int>& nums)
	{
		int n = nums.size();
		int i = n - 2;
		for (; i >= 0; --i)
		{
			if (nums[i] < nums[i + 1])break;
		}  // find the right
		int j = n - 1;
		if (i >= 0)
		{
			while (nums[j]<=nums[i])j--;
			swap(nums[i], nums[j]); // swap with the smallest bigger than nums[i]
		} 
		reverse(nums.begin()+i+1, nums.end()); // reverse the sorted nums to get the smallest nubmer
	}
};
int main()
{
	Solution sol;
	vector<int> nums = { -2};
	nums = { 3, 2, -2, 4 };
	//nums = { -4, -3 };
	nums = {1,2,3};
	sol.nextPermutation(nums);
	for (auto k : nums)cout << k << " ";
	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
