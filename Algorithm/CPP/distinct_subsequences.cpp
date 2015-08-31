# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
	int numDistinct1(string s, string t) {
		int m = t.size();
		int n = s.size();
		if (m > n) return 0;
		vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
		for (int i = 0; i <=n; i++)
			dp[0][i] = 1;
		for (int j = 0; j < n; j++)
			for (int i = 0; i < m; i++)
				dp[i + 1][j + 1] =  dp[i + 1][j] + (s[j] == t[i] ? dp[i][j] : 0);
		return dp[m][n];
	}
	int numDistinct(string s, string t) {
		int m = t.size();
		int n = s.size();
		if (m > n) return 0;
		vector<int> dp(m+1,0);
		dp[0] = 1;
		for (int j = 0; j < n; j++)
		{
			for (int i = min(j, m - 1); i >= 0; i--)
				dp[i + 1] = dp[i + 1] + (s[j] == t[i] ? dp[i] : 0);
		}
		return dp[m];
	}
		int numDistinct3(string s, string t) {
		int m = t.size();
		int n = s.size();
		if (m > n) return 0;
		vector<int> dp(m + 1, 0);
		dp[0] = 1;
		for (int j = 0; j < n; j++)
		{
			for (int i = min(j, m - 1); i >= 0; i--)
				dp[i + 1] = dp[i + 1] + (s[j] == t[i] ? dp[i] : 0);
		}
		return dp[m];
	}
};


int main()
{
	Solution sol;
	vector<int> nums = {1,2,3,1};
	string s = "ccc";
	string t = "cc";
	cout << sol.numDistinct(s,t);

	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
