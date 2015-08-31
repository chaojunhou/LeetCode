# include <vector>
# include <algorithm>
# include <string>
# include <stack>
# include <algorithm>
# include <deque>
# include <iostream>
using namespace std;


class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
 		vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
		dp[m - 1][n] = 1;
		for (int i = m - 1; i >= 0; --i)
			for (int j = n - 1; j >= 0; --j)
			
				dp[i][j] = obstacleGrid[i][j]==0? dp[i + 1][j] + dp[i][j + 1]:0;

		return dp[0][0];       
    }
};
