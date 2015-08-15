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
	vector<vector<int>> permuteUnique(vector<int>& nums)
	{
		vector<vector<int>> res;
		sort(nums.begin(), nums.end());
		dfs(res, 0, 1, nums);
		return res;
	}

	void dfs(vector<vector<int>>& res, int start, int depth,vector<int> nums)
	{
		if (depth == nums.size())
		{
			res.push_back(nums);
			return;
		}
		for (auto i = start; i != nums.size(); ++i)
		{
			if (i == start || nums[i] != nums[start])
			{
				swap(nums[i], nums[start]);
				dfs(res, start + 1, depth + 1, nums);
				//swap(nums[i], nums[start]);
			}
		}
	}
};
int  main()
{
	Solution sol;
	vector<int> nums1;
	for (int i = 0; i < 1; ++i)
	{
		nums1.push_back(rand() % 100);

	}

	nums1 = { 3, 3, 0, 0, 2, 3, 2 };
	sort(nums1.begin(), nums1.end());
	for (auto num1 : nums1) cout << num1 << " ";
	cout << endl;
	cout << " the answer is :" << endl;
	for (auto res : sol.permuteUnique(nums1))
	{
		for (auto num : res) cout << num << " ";
		cout << endl;
	}
	cout<< endl;
	cin.get();
	return 0;
}
