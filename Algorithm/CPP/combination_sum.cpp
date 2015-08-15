# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	vector<vector<int>> combinationSum(vector<int>& candidates, int target)
	{
		vector<vector<int>> res;
		sort(candidates.begin(), candidates.end());
		vector<int> ans;
		dfs(res, candidates, target, ans,0);
		return res;
	}

	void dfs(vector<vector<int>>& res, vector<int>& candidates, int target, vector<int> ans,int start)
	{
		if (target == 0)
		{
			res.push_back(ans);
			return;
		}
		for (int i = start; i != candidates.size() && target>=candidates[i]; ++i)
		{
		//	if (target < candidates[i]) return;
			ans.push_back(candidates[i]);
			dfs(res,candidates,target-candidates[i],ans,i);
			ans.pop_back();
		}
	}
	vector<vector<int>> combinationSum1(vector<int>& candidates, int target)
	{
		vector<vector<int>> res;
		sort(candidates.begin(), candidates.end());
		vector<int> ans;

		dfs1(res, candidates, target, ans);


		return res;

	}
	void dfs1(vector<vector<int>>& res, vector<int>& candidates, int target,vector<int> ans)
	{
		if (target == 0)
		{
			sort(ans.begin(), ans.end());
			if (find(res.begin(),res.end(),ans) == res.end())
				res.push_back(ans);
			return;
		}
		for (auto candidate : candidates)
		{
			if (candidate > target) return;
			ans.push_back(candidate);
			dfs1(res, candidates, target - candidate, ans);
			ans.pop_back();
		}
	}
};
int  main()
{
	Solution sol;
	vector<int> candidates = { 2,3,6,7};
	int target = 7;
	candidates = { 1, 2 };
	target = 4;
	auto vec = sol.combinationSum(candidates, target);
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
