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

	vector<vector<int>> subsetwithDup(vector<int>& nums)
	{
		vector<vector<int>> res;
		sort(nums.begin(), nums.end());
		vector<int> ans;
		dfs(res, nums, ans,0);
		return res;
	}
	void dfs(vector<vector<int>>& res, vector<int>& nums, vector<int> ans,int start)
	{

		res.push_back(ans);
		int pre = -1;
		for (int i = start; i < nums.size(); ++i)
		{
			if (pre != nums[i])
			{
				ans.push_back(nums[i]);
				pre = nums[i];
				dfs(res, nums, ans, i + 1);
				ans.pop_back();
			}
		}
	}

};


int main()
{
	Solution sol;
	vector<int> triangle = { 1,2,1,3,2,5};
	triangle = { 2, 1, 2, 3, 4, 1 };
	triangle = { 1, 2, 2 };
	for (auto k : sol.subsetwithDup(triangle))
	{
		for (auto x:k)	cout << x << " ";
		cout << endl;
	}
	system("pause");
	return 0;
}
