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
		string addBinary1(string a, string b)
		{
			int m = a.size();
			int n = b.size();
			int c = 0;
			string res;
			while (m && n)
			{
				if (a[--m] == '1')
				{
					c += 1;
				}
				if (b[--n] == '1')
				{
					c += 1;
				}
				res = char(c % 2 + '0') + res;
				c /= 2;
			}
			while (m)
			{
				if (a[--m] == '1')
				{
					c += 1;
				}
				res = char(c % 2 + '0') + res;
				c /= 2;
			}
			while (n)
			{
				if (b[--n] == '1')
				{
					c += 1;
				}
				res = char(c % 2 + '0') + res;
				c /= 2;
			}
			if (c) res = '1' + res;
			return res;
		}
		string addBinary(string a, string b)
		{
			string res;
			int c = 0, i = a.size()-1, j = b.size()-1;
			while (i>=0 || j>=0 || c==1)
			{
				if (i >= 0)
				{
					if (a[i--] == '1') c += 1;
				}
				if (j >= 0)
				{
					if (b[j--] == '1') c += 1;
				}
				res = char(c % 2 + '0') + res;
				c /= 2;
			}
			return res;
		}
};
int  main()
{
	Solution sol;
	cout<< sol.addBinary("10","11")<<endl;
	cin.get();
	return 0;
}
