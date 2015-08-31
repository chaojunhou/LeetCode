# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;

class Solution {
public:
	int minimumTotal(vector<vector<int>>& triangle) {
		int m = triangle.size();
		vector<int> dp(triangle[m-1]);
		for (int i = m - 2; i >= 0; --i)
		{
			for (int j = 0; j <= i; ++j)
			{
				dp[j] = min(dp[j], dp[j+ 1]) + triangle[i][j];
			}
		}
		return dp[0];
	}
};


int main()
{
	Solution sol;
	vector<vector<int>> triangle = { { 2 }, { 3, 4 }, {6,5,7}
	, { 4, 1, 8, 3 } };
	cout << sol.minimumTotal(triangle);
	system("pause");
	return 0;
}
