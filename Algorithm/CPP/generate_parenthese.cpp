
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
	vector<string> generateParenthesis(int n) {
		vector<string> res;
		string ans;
		dfs(res, ans, n, 0, 0);
		return res;
	}
	void dfs(vector<string>& res, string ans,int n, int left, int right)
	{
		if (left > n || right > n) return;
		if (left == n && right == n)
		{
			res.push_back(ans); 
			//return;
		}
		if (right > left) return;
		if (left>right) dfs(res, ans + ')', n, left, right + 1);
		if(left<n)	dfs(res, ans + '(', n, left+1, right);
		
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1, 1, 1, 3, 3, 2, 2, 2};
	//nums = { 1, 2 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	string word1 = "vintner";
	string word2 = "writers";
	for( auto k:sol.generateParenthesis(3)) cout<<k<< endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
