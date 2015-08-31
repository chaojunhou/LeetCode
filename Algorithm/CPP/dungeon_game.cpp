# include <vector>
# include <iostream>
using namespace std;

class Solution {
public:
	int calculateMinimumHP(vector<vector<int>>& dungeon) {
		int m = dungeon.size();
		int n = dungeon[0].size();
		vector<vector<int>> dp(m+1,vector<int>(n+1,INT_MAX));
		dp[m][n - 1] = 1;
		dp[m - 1][n] = 1;
		int need;
		for (int i = m - 1; i >= 0; i--)
			for (int j = n - 1; j >= 0; j--)
			{
				dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j],1);
			}
		return dp[0][0];

	}
};
int main()
{
	Solution sol;
	vector<int> nums = { -2};
	nums = { 3, 2, -2, 4 };
	//nums = { -4, -3 };
	nums = {1,2,3};
	vector < vector<int>> dungeon = {
		{-2,-3,3},
		{-5,-10,1},
		{10,30,-5}
	};
	dungeon = { { -1, 1 } };
	//dungeon = { { -200 } };
	cout << sol.calculateMinimumHP(dungeon);
	
	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
