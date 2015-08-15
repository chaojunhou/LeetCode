# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	void setZeroes(vector<vector<int>>& matrix)
	{
		vector<bool> row(matrix.size()), col(matrix[0].size());
		for (auto i = 0; i != matrix.size(); ++i)
			for (auto j = 0; j != matrix[0].size(); ++j)
			{
				if (matrix[i][j] == 0)
				{
					row[i] = true;
					col[j] = true;
				}
			}
		for (auto i = 0; i != matrix.size(); ++i)
			for (auto j = 0; j != matrix[0].size(); ++j)
			{
				if (row[i] || col[j] )
				{
					matrix[i][j] = 0;
				}
			}

	}

};
int  main()
{
	Solution sol;
	vector<vector<int>> candidates = { { 2, 3, 6, },{ 7,0,1 }, { 4, 2, 0 }  };
	sol.setZeroes(candidates);
	for (auto k : candidates)
	{
		for (auto x : k)
		{
			cout << x << ", ";
		}

		cout << endl;
	}


	cin.get();
	return 0;
}
