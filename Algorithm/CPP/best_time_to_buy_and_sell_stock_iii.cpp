//# include <vector>
//# include <algorithm>
//# include <string>
//# include <deque>
//# include <iostream>
# include <vector>
# include <algorithm>
# include <string>
# include <deque>
# include <iostream>
using namespace std;







class Solution {
public:
    int maxProfit(vector<int>& prices) {
		int res;
		int n = prices.size();
		if (n < 2)return 0;
		//k = 2;
		vector<vector<int>> dp(3, vector<int>(n, 0));
		for (int j = 1; j <= 2; j++)
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

