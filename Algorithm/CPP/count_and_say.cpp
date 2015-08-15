# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
using namespace std;
class Solution {

public:
	string getNumber(string s)
	{

		string res;

		char pre = s[0];
		char ch = pre;
		int count = 0;
		for (auto chr:s)
		{
			ch = chr;
			if (ch != pre)
			{
				res += to_string(count) + pre;
				count = 1;
				pre = ch;
			}
			else
			{
				count += 1;
			}
		}
		res += to_string(count) + ch;
		return res;

	}
	string countAndSay(int n)
	{
		string  number = "1";
		for (auto i = 0; i < n-1; ++i)
		{
			number =getNumber(number);
		}
		return number;
	}
};
int  main()
{
	Solution sol;
	int n = 40;
	//cout << char(2 + '0') << endl;
	cout << sol.countAndSay(n) << endl;
	cin.get();
	return 0;
}
