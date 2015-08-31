# include<stdio.h>
# include <iostream>
# include <string>
# include <array>
# include <vector>
using namespace std;


class Solution {
public:
	int minPathSum(vector<vector<int>>& grid) {
		int m = grid.size();
		int n = grid[0].size();
		vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MAX));
		dp[0][1] = 0;
		dp[1][0] = 0;
		for (int i = 0; i < m; i++)
			for (int j = 0; j < n; j++)
			{
				dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j];
			}
		return dp[m][n];

	}
};
int main()
{
	Solution sol;
	vector<int> nums = { -2};
	nums = { 3, 2, 2, 4 };
	//nums = { -4, -3 };
	nums = {1,2,3};
	vector < vector<int>> dungeon = {
		{2,3,3},
		{5,10,1},
		{10,30,5}
	};
	//dungeon = { { -1, 1 } };
	//dungeon = { { -200 } };
	cout << sol.minPathSum(dungeon);
	
	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
