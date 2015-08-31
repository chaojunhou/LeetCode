
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
	string longestPalindrome(string s)
	{
		string res;
		int start = 0;
		int end = 0;
		for (int i = 0; i < s.size(); ++i)
		{
			int len = max(expand(s, i, i), expand(s, i, i + 1));
			if (len > end - start)
			{
				start = i - (len - 1) / 2;
				end = i + len / 2;
			}
		}

		return s.substr(start,end-start+1);

		
	}
	int expand(string& s, int left, int right)
	{
		while ((left >= 0) && (right<s.size()) && (s[left] == s[right]))
		{
			left--;
			right++;
		}
		return right-left-1;
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
	string s = "aab";	
	cout << sol.longestPalindrome(s) << endl;

	system("pause");
	return 0;
}

