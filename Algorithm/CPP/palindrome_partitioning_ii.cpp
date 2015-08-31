# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

class Solution {
public:
	int minCut(string s)
	{
		int n = s.size();
		vector<int> dp(n + 1,0);
		for (int i = 0; i < n + 1; ++i) dp[i] = i - 1; // initimate the vecotre
		for (int i = 0; i < n; i++)
		{
		
			for (int j = 0; (i + j < n) && (j <= i); j++)
			{
				if (s[i - j] == s[i + j])	   dp[i + j + 1] = min(dp[i + j + 1], 1 + dp[i - j]);
				else break;
			}
			for (int j = 1; (i + j < n)&& (i-j+1>=0); j++)
			{
				if (s[i - j + 1] == s[i + j])  dp[i + j + 1] = min(dp[i + j + 1], 1 + dp[i - j + 1]);
				else break;
			}
		}
		return dp[n];
	}
	int minCut1(string s) {
		if (s.empty()) return 0;
		int n = s.size();
		vector<vector<bool>> palindrome(n, vector<bool>(n, false));
		vector<int> dp(n);
		for (int i = 0; i < n; ++i)
		{
			dp[i] = n - (i + 1);
		}
		for (int i = n - 1; i >= 0; i--)
		{
			for (int j = i; j < n; j++)
			{
				if (s[i] == s[j] && (j - i < 2 || palindrome[i + 1][j - 1])) //the st[i+1,...j-1] is the palindrome 
				{
					palindrome[i][j] = true;
					if (j == n - 1) dp[i] = 0;
					else dp[i] = min(dp[i], 1 + dp[j + 1]);
				}
			}
		}
		return dp[0];
	}
};
int main()
{
	Solution sol;
	vector<int> nums = { 4, 1, 2, 7, 5, 3, 1};
	//nums = { 1, 2 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	string word1 = "vintner";
	string word2 = "writers";

	string s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
	int n = sol.minCut("cabababcbc");
	cout<<n<<endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
