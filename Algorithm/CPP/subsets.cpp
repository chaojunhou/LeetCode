//# include <vector>
//# include <algorithm>
//# include <string>
//# include <deque>
//# include <iostream>
# include <vector>
# include <algorithm>
# include <string>
# include <deque>
# include <iostream>
using namespace std;


class Solution {
public:
	vector<vector<int>> subsets(vector<int>& nums)
	{
		
		sort(nums.begin(), nums.end());
		int n = nums.size();
		int resLen = pow(2, n);
		vector<vector<int>> res(resLen, vector<int>());
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < resLen; ++j)
			{
				if ((j>>i) & 1)
				{
					res[j].push_back(nums[i]);
				}
			}
		}
		return res;
	}
	vector<vector<int>> subsets1(vector<int>& nums)
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
		for (int i = start; i < nums.size(); ++i)
		{
			
			ans.push_back(nums[i]);
			dfs(res, nums, ans, i + 1);
			ans.pop_back();
		}
	}

};


int main()
{
	Solution sol;
	vector<int> triangle = { 1,2,1,3,2,5};
	triangle = { 2, 1, 2, 3, 4, 1 };
	triangle = { 1, 2, 3 };
	for (auto k : sol.subsets(triangle))
	{
		for (auto x:k)	cout << x << " ";
		cout << endl;
	}
	system("pause");
	return 0;
}



