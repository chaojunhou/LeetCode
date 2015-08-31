# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;




class Solution {
public:
	vector<vector<string>> solveNQueens(int n) {
		vector<vector<string>> res;
		vector<int> ans(n,0) ;
		dfs(res, 0, 0, ans,n);
		return res;
	}
	void dfs(vector<vector<string>>& res, int start, int depth, vector<int> ans, int n)
	{
		if (depth == n)
		{
			vector<string> tmp;
			for (int i = 0; i < n; ++i)
			{
				tmp.push_back(string(ans[i], '.') + 'Q' + string(n - ans[i]-1, '.'));
			}
			res.push_back(tmp);
			return;
		}
		for (int j = 0; j < n; ++j)
		{
			int i = 0;;
			for (; i < start; ++i)
			{
				if (ans[i] == j || (abs(start - i) == abs(j - ans[i]))) // same row or same col
				{
					break;
				}
			}
			if (i == start)
			{
				ans[depth] = j;
				dfs(res, start + 1, depth + 1, ans, n);
			}
		}
	}
};

int main()
{
	Solution sol;
	string s = "ADOBECODEBANC";
	for (auto k : sol.solveNQueens(4))
	{
		for (auto x : k)
			cout << x << " ";
		cout << endl;
	}

	system("pause");
	return 0;
}
