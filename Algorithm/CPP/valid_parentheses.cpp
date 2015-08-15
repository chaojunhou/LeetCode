# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <stack>
# include <algorithm>
# include<time.h>
using namespace std;


class Solution {
public:
	bool isValid(string s) {
		stack<char> Stack;
		for (auto chr : s)
		{
			if (chr == '(' || chr == '[' || chr== '{')
				Stack.push(chr);
			if (chr == ')' || chr == ']' || chr == '}')
			{
				if (Stack.empty()) return false;
				if (chr == ')')
				{
					if (Stack.top() != '(') return false;
				}
				else if (chr == ']'){
					if (Stack.top() != '[') return false;
				}
				else {
					if (Stack.top() != '{') return false;
				}
				Stack.pop();
			}
				
		}
		return Stack.empty();
	}
};
int  main()
{
	Solution sol;

	//nums = { -1 };
	cout << sol.isValid("([)]");
	cin.get();
	return 0;
}

