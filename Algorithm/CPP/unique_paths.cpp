# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	int uniquePaths(int m, int n) 
	{
		vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
		dp[m - 1][n] = 1;
		for (int i = m - 1; i >= 0; --i)
			for (int j = n - 1; j >= 0; --j)
				dp[i][j] = dp[i + 1][j] + dp[i][j + 1];

		return dp[0][0];
	}
};
int  main()
{
	Solution sol;

	string path = "/a/./b/../../c/";
	//path = "/";
	path = "/...";
	path = "A man, a plan, a canal: Panama";
	path = " ";
	path = "1a2";

	cout << sol.uniquePaths(4,5) << endl;
	system("pause");
	return 0;
}
