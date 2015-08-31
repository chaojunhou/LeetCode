# include<stdio.h>
# include <iostream>
# include <string>
# include <array>
# include <vector>
using namespace std;

class Solution {
public:
	int longestValidParentheses(string s) {
		stack<int> Stack;
		int res = INT_MIN;
		int n = s.size();
		for (int i = 0; i < n; i++)
		{
			if (s[i] == '(')
			{
				Stack.push(i);
			}
			else
			{
				if (!Stack.empty())
				{
					if (s[Stack.top()] == '(')			Stack.pop();
					else Stack.push(i);
				}
				else
					Stack.push(i);
			}
		}
		if (Stack.empty()) return n;
		int len;
		int i;
		while (!Stack.empty())
		{
			i = Stack.top();
			Stack.pop();
			len = n - i - 1;
			n = i;
			res = max(len, res);
		}
		res = max(res, i);
		return res;
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { -2};
	nums = { 3, 2, 2, 4 };
	//nums = { -4, -3 };
	nums = {1,2,3};
	vector < vector<int>> dungeon = {
		{2,3,3},
		{5,10,1},
		{10,30,5}
	};
	//dungeon = { { -1, 1 } };
	//dungeon = { { -200 } };
	string s = "(()";
	s = "())";
	cout << sol.longestValidParentheses(s);
	
	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}

