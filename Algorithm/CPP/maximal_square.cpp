# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

class Solution{
public:
	int maximalSquare(vector<vector<char>>& matrix){
		int m = matrix.size();
		if (m < 1) return 0;
		int n = matrix[0].size();
		vector<vector<int>> dp(m, vector<int>(n, 0));
		int maxSize = 0;
		for (int i = 0; i < m;i++)
		{
			dp[i][0] = matrix[i][0]-'0';
			if (dp[i][0]) maxSize = 1;
		}
		
		for (int j = 1; j < n; j++)
		{
			dp[0][j] = matrix[0][j] - '0';
			if (dp[0][j]) maxSize = 1;

		}		
		for (int i = 1; i < m; i++)
			for (int j = 1; j < n; j++)
			{
				if (matrix[i][j]=='1')
				{
					dp[i][j] = min(min(dp[i - 1][j], dp[i - 1][j - 1]), dp[i][j - 1]) + 1;
					if (dp[i][j] > maxSize)
						maxSize = dp[i][j];
				}
			}
		return maxSize*maxSize;
	}
};



int main()
{
	Solution sol;
	vector<vector<char>> matrix = {
		{'1','0','1','0','0'},
		{'1','0','1','1','1'},
		{'1','1','1','1','1'},
		{ '1', '0', '0', '1', '0' }
	};
	matrix = { { '0', '1' } };
	cout << sol.maximalSquare(matrix) << endl;

	system("pause");
	return 0;
}

