# include<stdio.h>
# include <iostream>
# include <string>
# include <array>
# include <vector>
using namespace std;
class Solution {
public:
	vector<vector<int>> generateMatrix(int n) {

		vector<vector<int>> matrix(n, vector<int>(n));
		int counter = 0;
		int row = 0, col = -1;
		int square = n*n;
		while (1)
		{
			for (int i = 0; i<n; ++i)
			{
				counter += 1;
				col += 1;
				matrix[row][col] = counter;
			}
			n -= 1;
			for (int i = 0; i<n; ++i)
			{
				counter += 1;
				row += 1;
				matrix[row][col] = counter;
			}
			for (int i = 0; i<n; ++i)
			{
				counter += 1;
				col -= 1;
				matrix[row][col] = counter;
			}
			n -= 1;
			for (int i = 0; i<n; ++i)
			{
				counter += 1;
				row -= 1;
				matrix[row][col] = counter;
			}
			if (counter == square)
				return matrix;
		}

	}
};
int main()
{
	Solution sol;
	int n = 3;
	auto vec = sol.generateMatrix(n);
	for (int i = 0; i < vec.size(); ++i)
	{
	for (int j = 0; j < vec[0].size(); ++j)
		cout << vec[i][j] << "";
	cout << endl;
	}


	return 0;
}
