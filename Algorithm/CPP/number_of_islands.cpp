# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;


class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
		int m = grid.size();
		if (m < 1) return 0;
		int n = grid[0].size();
		int res = 0;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (grid[i][j] == '1')
				{
					dfs(grid, i, j);
					res++;
				}
			}
		}
		return res;
	}
	void dfs(vector<vector<char>>& grid, int row, int col)
	{
		
		if (row>0 && grid[row - 1][col] == '1')
		{
			grid[row - 1][col] = 'X';
			dfs(grid, row - 1, col);
		}
		if (col>0 && grid[row][col - 1] == '1')
		{
			grid[row][col - 1] = 'X';
			dfs(grid, row, col - 1);
		}
		if (row < grid.size()-1 && grid[row + 1][col] == '1')
		{
			grid[row + 1][col] = 'X';
			dfs(grid, row + 1, col);
		}
		if (col < grid[0].size() - 1 &&grid[row][col + 1] == '1')
		{
			grid[row][col + 1] = 'X';
			dfs(grid, row, col + 1);
		}
			
	}
};
