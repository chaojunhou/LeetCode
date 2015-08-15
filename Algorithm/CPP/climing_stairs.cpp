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

	int climbStairs(int n) {
		if (n == 0) return 0;
		vector<int> dp(3, 1);
		for (int i = 2; i <= n; ++i)
		{
			dp[2] = dp[1] + dp[0] ;
			dp[0] = dp[1];
			dp[1] = dp[2];
		}
		return dp[2];
	}
};


int main()
{
	Solution sol;


	int target = 7;

	cout << sol.climbStairs(target) << endl;

	system("pause");
	return 0;
}
