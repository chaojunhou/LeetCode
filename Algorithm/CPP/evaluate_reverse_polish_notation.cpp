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
	int evalRPN(vector<string>& tokens) {
		stack<int> Stack;
		int tmp = 0;
		int top1 = 0;
		int top2 = 0;
		for (string token : tokens)
		{
			if ((token == "+") || (token == "-") || (token == "*") || (token == "/"))
			{
				top1 = Stack.top();
				Stack.pop();
				top2 = Stack.top();
				Stack.pop();
				if (token == "+")
				{
					tmp = top2 + top1;
				}
				if (token == "-")
				{
					tmp = top2 - top1;
				}
				if (token == "*")
				{
					tmp = top2 * top1;
				}
				if (token == "/")
				{
					tmp = top2 / top1;
				}
				Stack.push(tmp);
			}
			else
			{
				Stack.push(stoi(token));
			}
		}
		return Stack.top();
	}
};
int main()
{
	Solution sol;
	vector<string> tokens = {"4","13","5","/","+"};
	cout << sol.evalRPN(tokens) << endl;
	
	system("pause");
	return 0;
}
