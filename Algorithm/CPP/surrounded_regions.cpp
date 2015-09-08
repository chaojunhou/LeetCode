# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	void solve(vector<vector<char>>& board) {
		int row = board.size();
		if (!row) return;
		int col = board[0].size();
		for (int i = 0; i < row; i++)
		{
			dfs(board, i, 0);
			if (col>1)	dfs(board, i, col - 1);
		}
		for (int j = 1; j < col; j++)
		{
			dfs(board, 0, j);
			if (row>1)	dfs(board, row - 1, j);
		}
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				if (board[i][j] == 'O')
				{
					board[i][j] = 'X';
				}
			}
		}
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				if (board[i][j] == '#') board[i][j] = 'O';
			}
		}
	}
	void dfs(vector<vector<char>>& board, int row, int col)
	{
		if (board[row][col] == 'O')
		{
			board[row][col] = '#';
			if (row > 1) dfs(board, row - 1, col);
			if (col > 1) dfs(board, row, col - 1);
			if (row < board.size() - 1) dfs(board, row + 1, col);
			if (col < board[0].size() - 1) dfs(board, row, col + 1);
		}
	}

};
int main()
{
	Solution sol;
	vector<int> res = { 3,0,6,1,5 };
	vector<vector<char>> board;
	board = {
		{ 'X', 'X', 'X', 'X' },
		{ 'X', 'O', 'O', 'X' },
		{ 'X', 'X', 'O', 'X' },
		{ 'X', 'O', 'X', 'X' },
	};
	sol.solve(board);
	for (int i = 0; i < board.size(); i++)
	{
		for (int j = 0; j < board[0].size(); j++)
		{
			cout<<board[i][j] << " ";
		}
		cout<<endl;
	}

	system("pause");
	return 0;

}
