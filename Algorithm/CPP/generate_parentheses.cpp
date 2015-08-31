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
	bool isPalindrome(string s) {
		int left = 0;
		int right = s.size() - 1;
		while (left <=
			right)
		{
			while ((ispunct(s[left]) || s[left] == ' ')){ left++; if (left == s.size()) return true; }

			while ((ispunct(s[right]) || s[right] == ' ')){ right--; if (right < left) return true; }

			if (tolower(s[left]) == tolower(s[right]))
			{
				left++;
				right--;
			}
			else
			{
				return false;
			}

		}
		return true;
	}
	vector<vector<string>> partition(string s) 
	{
		vector<vector<string>> res;
		vector<string> ans;
		dfs(res, s, ans,0);
		return res;
	}
	void dfs(vector<vector<string>>& res, string& s, vector<string> ans,int start)
	{
		if (start == s.size())
		{
			res.push_back(ans);
			return;
		}
		for (int i = 1; i <= s.size()-start; ++i)
		{

			if (isPalindrome(s.substr(start, i)))
			{
				//cout << s.substr(start, i);
				ans.push_back(s.substr(start, i));
				dfs(res, s, ans, start + i);
				ans.pop_back();
			}
		}
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
	for (auto k : sol.partition(s))
	{
		for (auto x : k)
			cout << x << " ";
		cout << endl;
	} 
	system("pause");
	return 0;
}
