# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int largestRectangleArea(vector<int>& height) {
		stack<int> Stack;
		height.push_back(-1);
		int n = height.size();
		int i = 0;
		int res=0;
		int top;
		while (i < n)
		{
			if (Stack.empty() || height[i] >= height[Stack.top()])
			{
				Stack.push(i);
				i++;
			}
			else
			{
				top = Stack.top();
				Stack.pop();
				
				if (Stack.empty()) res = max(res, i*height[top]);
				else  res = max(res, (i - Stack.top() - 1)*height[top]);
			}
		}
		return res;

	}
};



int main()
{
	Solution sol;
	vector<vector<char>> matrix = {
		{'1','0','1','0','0'},
		{'1','0','1','1','1'},
		{'1','1','1','1','1'},
		{ '1', '0', '0', '1', '0' }
	};
	matrix = { { '0', '1' } };
	vector<int> height = { 2, 1, 5, 6, 2, 3 };
	//height = { 1 };
	height = { 4,2 };
	cout << sol.largestRectangleArea(height) << endl;


	system("pause");
	return 0;
}

