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
	int minDistance(string word1, string word2) {
		int m = word1.size();
		int n = word2.size();
		vector<vector<int>> dp(m+1, vector<int>(n+1));

		for (int i = 0; i < m+1; ++i)
		{
			dp[i][0] = i;
		}
		for (int j = 0; j < n+1; ++j)
		{
			dp[0][j] = j;
		}
		for (int i = 0; i < m; ++i)
			for (int j = 0; j < n; ++j)
			{
				if (word1[i] == word2[j])
				{
					dp[i+1][j+1] = min(min(dp[i][j+1], dp[i+1][j]) + 1, dp[i][j]);
				}
				else
				{
					dp[i+1][j+1] = min(dp[i][j], min(dp[i+1][j], dp[i][j+1])) + 1;
				}
			}
		return dp[m][n];

	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1, 1, 1, 3, 3, 2, 2, 2};
	//nums = { 1, 2 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	string word1 = "vintner";
	string word2 = "writers";
	cout<<sol.minDistance(word1,word2)<< endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}

