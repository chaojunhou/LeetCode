# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

class Solution {
public:
	int numDecodings(string s) {
	
		if (s == "" || s[0] == '0') return 0;
		int n = s.size();
		vector<int> dp(n+1, 1);
		for (int i = 0; i <= n-2; ++i)
		{
			string tmp = s.substr(i, 2);
			if ("10" <= tmp && tmp <= "26")
			{
				if ((tmp == "10") || (tmp == "20"))
				{
					dp[i + 2] = dp[i];
				}
				else
				{
					dp[i + 2] = dp[i + 1] + dp[i];
				}
			}
			else if (s[i + 1] != '0') // 27,32
			{
				dp[i + 2] = dp[i + 1];
			}
			else // 00,30,40,50,60,70,80,90,
			{
				return 0;
			}

		}
		return dp[n];
	}
};


int main()
{
	Solution sol;
	vector<int> nums = {1,1,1,0,1
	};
	//cout << sol.numDecodings("101") << endl;
	//cout << sol.numDecodings("100") << endl; 
	//cout << sol.numDecodings("227") << endl;
	cout << sol.numDecodings("72206") << endl; //1
	//0
	system("pause");
}
