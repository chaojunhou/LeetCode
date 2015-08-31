# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;

class Solution {
public:

	vector<string> restoreIpAddresses(string s) {
		vector<string> res;
		string ans;
		dfs(res, s,ans, 0,0);
		return res;
	}
	void dfs(vector<string>& res, string s, string ans,int idx, int depth)
	{
		if (depth > 4) return;
		if ((depth == 4) && (idx == s.size()))
		{
			res.push_back(ans.substr(1,ans.size()-1));
			return;
		}
		
		for (int i = 1; i < 4; ++i)
		{
			if (s[idx] == '0' && i>1) return;
			if (idx + i > s.size()) return;
			string tmp = s.substr(idx, i);
			if (stoi(tmp) < 256)
			{						
				dfs(res, s, ans+"." + tmp, idx + i, depth + 1);
			}
			else
			{
				return;
			}
		}		
	}
};


int main()
{
	Solution sol;
	cout << endl;
	for (auto s : sol.restoreIpAddresses("010010"))
		cout << s << endl;
	system("pause");
	return 0;
}
