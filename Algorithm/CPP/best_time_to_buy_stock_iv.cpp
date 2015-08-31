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
    int maxProfit(int k, vector<int>& prices) {
  		int res;
		int n = prices.size();
		if (n < 2)return 0;
		//k = 2;
		if (k > n / 2)
		{
			for (int i = 1; i < n; i++)
			{
				if (prices[i - 1] < prices[i]) res += (prices[i] - prices[i - 1]);
			}
			return res;
		}
		vector<vector<int>> dp(k + 1, vector<int>(n, 0));
		for (int j = 1; j <= k; j++)
		{
			int tmpMax = dp[j - 1][0] - prices[0];
			for (int i = 1; i < n; i++)
			{
				dp[j][i] = max(dp[j][i - 1], prices[i] + tmpMax);
				tmpMax = max(tmpMax, dp[j-1][i] - prices[i]);
				res = max(res, dp[j][i]);
			}
		}
		return res;      
    }
};
