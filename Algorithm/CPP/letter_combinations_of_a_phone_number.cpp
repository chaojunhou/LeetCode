# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

class Solution {
	public:
		vector<string> letterCombinations(string digits)
		{

			vector<string> res;
			if (digits.size() == 0) return res;
			vector<string> dict = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
			string ans;
			dfs(res, dict, 0, digits, ans);
			return res;
		}
		void dfs(vector<string>& res, vector<string>& dict, int depth, string digits, string ans)
		{
			if (depth == digits.size())
			{
				res.push_back(ans);
				return;
			}
			for (auto chr : dict[digits[depth] - '0'])
			{
				dfs(res, dict, depth + 1, digits, ans + chr);
			}
		}
};
int  main()
{
	Solution sol;
	for (auto s : sol.letterCombinations("23")) cout << s << " ";
	cout<< endl;
	cin.get();
	return 0;
}
