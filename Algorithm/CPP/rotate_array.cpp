# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;



class Solution {
public:
	void rotate(vector<int>& nums, int k) {
		k = k % (nums.size());
		reverse(nums, 0, nums.size() - 1);
		reverse(nums, 0, k - 1);
		reverse(nums, k, nums.size() - 1);
	}
	void reverse(vector<int>& nums, int start, int end)
	{
		while (start < end)
		{
			int tmp = nums[start];
			nums[start] = nums[end];
			nums[end] = tmp;
			start++;
			end--;			
		}
	}
};
int  main()
{
	Solution sol;
	vector<int> nums = { 1, 2, 3, 4, 5, 6, 7};
	int k = 3;
	sol.rotate(nums, k);

	for (auto i : nums) cout << i << " ";
	cout << endl;
	system("pause");
	return 0;
}
