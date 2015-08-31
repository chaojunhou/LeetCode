# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

class Solution {
public:

	string shortestPalindrome(string s)
	{
		int m = s.size();
		string t(s);
		reverse(t.rbegin(), t.rend());		
		int j = -1;
		vector<int> prefix;
		prefix= compute_prefix(s);

		
		for (int i = 0; i < m; ++i)
		{
			while (j > -1 && (s[j + 1] != t[i]))
			{
				j = prefix[j];
			}
			if (s[j + 1] == t[i])
				j += 1;

		}

		
		return  t.substr(0,m-j-1) + s;
	}
	vector<int> compute_prefix(string& s)
	{
		int m = s.size();
		int j = -1;
		vector<int> prefix(m,-1);
		for (int i = 1; i < m; ++i)
		{
			while (j > -1 && (s[j + 1] != s[i]))
				j = prefix[j];
			if (s[j + 1] == s[i]) j += 1;
			prefix[i] =j;
		}
		return prefix;
	}
};

int main()
{
	Solution sol;
	vector<string> strs = { "eat", "tea", "tan", "ate", "nat", "bat" };
	string s = "abbacd";
	cout << sol.shortestPalindrome(s) << endl;
	system("pause");
	return 0;
}

