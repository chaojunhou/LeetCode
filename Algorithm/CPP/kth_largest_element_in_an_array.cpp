# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	vector<vector<int>> generate(int numRows) {
		vector<vector<int>> res(numRows);
		for (int i = 0; i < numRows; i++)
		{
			res[i].resize(i + 1,1);
			for (int j = 1; j < i; ++j)
			{
				res[i][j] = res[i - 1][j - 1] + res[i - 1][j];
			}
		}
		return res;
	}
};
int main()
{
	Solution sol;
	int numRows = 5;
	for (auto k : sol.generate(numRows))
	{
		for (auto x : k) cout << x << " ";
		cout << endl;
	}
	system("pause");
	return 0;
}

