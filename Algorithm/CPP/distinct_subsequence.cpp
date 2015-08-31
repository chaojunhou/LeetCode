# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;



class Solution {
public:
	int numDistinct(string s, string t) {
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
};

int main()
{
	Solution sol;
	vector<int> nums = {1,2,3,1};
	string s = "ccc";
	string t = "c";
	cout << sol.numDistinct(s,t);

	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}


