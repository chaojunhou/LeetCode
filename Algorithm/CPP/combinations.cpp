# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	vector<vector<int>> combine(int n, int k)
	{
		vector<vector<int>> res;
		vector<int> ans;
		helper(res,1, n, k, 0, ans);
		return res;

	}

	void helper(vector<vector<int>> & res,int from, int n, int k, int depth, vector<int>& ans)
	{

		if (depth == k)
		{
			res.push_back(ans);
			return;
		}
		for (auto i = from; i < n+1; ++i)
		{
			ans.push_back(i);//
			helper(res,i+1, n, k, depth + 1, ans);
			ans.pop_back();
		}

	}
};
int  main()
{
	Solution sol;
	auto vec = sol.combine(4,2);
	for (auto k : vec)
	{
		for (auto x : k)
		{
			cout << x << " ";
		}

		    cout << endl;
	}


	cin.get();
	return 0;
}
