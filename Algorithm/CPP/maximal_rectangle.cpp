# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int maximalRectangle(vector<vector<char>>& matrix) {
		int m = matrix.size();
		if (m < 1) return 0;
		int n = matrix[0].size();

		vector<int> rectangle(n + 1, 0);
		rectangle[n] = -1;

		int res = 0;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (matrix[i][j] == '1') rectangle[j] += 1;
				else rectangle[j] = 0;
			}
			stack<int> Stack;
			int k = 0;


			while (k < n + 1)
			{
				if (Stack.empty() || rectangle[k] >= rectangle[Stack.top()])
				{

					Stack.push(k);
					k++;
				}
				else
				{
					int top = Stack.top();
					Stack.pop();
					if (Stack.empty()) res = max(res, k*rectangle[top]);
					else res = max(res, (k - Stack.top() - 1)*rectangle[top]);
				}
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
	matrix = { { '1','0', '1', '0' }, { '1','0', '1', '1' }, 
	{ '1', '0', '1', '1' },
	{'1','1','1','1'} };
	//matrix = { { 0, 0 } };
	//matrix = { { '0' } };
	cout << sol.maximalRectangle(matrix) << endl;


	system("pause");
	return 0;
}

