# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	vector<vector<int>> combinationSum2(vector<int>& candidates, int target)
	{
		vector<vector<int>> res;
		sort(candidates.begin(), candidates.end());
		vector<int> ans;
		dfs(res, candidates, target, ans, 0);
		return res;
	}

	void dfs(vector<vector<int>>& res, vector<int>& candidates, int target, vector<int> ans, int start)
	{
		if (target == 0)
		{
			res.push_back(ans);
			return;
		}

		for (int i = start; i != candidates.size() && target >= candidates[i]; ++i)
		{
			if (i == start || candidates[i] != candidates[i - 1])  // the first time or not the same as before
			{
				ans.push_back(candidates[i]);
				dfs(res, candidates, target - candidates[i], ans, i + 1);
				ans.pop_back();
			}

		}
	}
};
int  main()
{
	Solution sol;
	vector<int> candidates = { 10, 1, 2, 7, 6, 1, 5 };
	int target = 8;
//	candidates = { 1, 1 };
//	target = 1;
	auto vec = sol.combinationSum2(candidates, target);
	for (auto k : vec)
	{
		for (auto x : k)
		{
			cout << x << ", ";
		}

		    cout << endl;
	}


	cin.get();
	return 0;
}
