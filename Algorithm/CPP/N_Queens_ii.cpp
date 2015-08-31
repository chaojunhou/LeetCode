# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int totalNQueens(int n) {
		int res = 0;
		vector<int> ans(n, 0);
		dfs(res, 0, ans, n);
		return res;
	}
	void dfs(int& res, int start, vector<int> ans, int n)
	{
		if (start == n)
		{
			res++;
			return;
		}
		for (int j = 0; j < n; ++j)
		{
			int i = 0;
			for (; i < start; ++i)
			{
				if (ans[i] == j || (abs(start - i) == abs(j - ans[i]))) // same row or same col
				{
					break;
				}
			}
			if (i == start)
			{
				ans[start] = j;
				dfs(res, start + 1, ans, n);
			}
		}
	}
};

int main()
{
	Solution sol;
	string s = "ADOBECODEBANC";
	int n = 12;
	cout << sol.totalNQueens(n) << endl;

	system("pause");
	return 0;
}
