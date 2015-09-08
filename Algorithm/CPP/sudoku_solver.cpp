
# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
using namespace std;



class Solution {
public:
	void solveSudoku(vector<vector<char>>& board) {
		solve(board);
	}
	bool solve(vector<vector<char>>& board)
	{
		int row = board.size();
		int col = board[0].size();
		for (int i = 0; i < row; i++)
			for (int j = 0; j < col; j++)
			{
				if (board[i][j] == '.')
				{
					for (int k = 1; k < 10; k++)
					{
						board[i][j] = k+'0';
						if (isValidSudoku(board) && solve(board)) return true;
						board[i][j] = '.';
					}
					return false;
				}
			}
		return true;
	}
	bool isValidSudoku(vector<vector<char>>& board) {
		int row = board.size();
		int col = board.size();
		int rows[9][9] = { 0 };
		int cols[9][9] = { 0 };
		int blocks[3][3][9] = { 0 };
		for (int i = 0; i < row; i++)
			for (int j = 0; j < col; j++)
			{
				if (board[i][j] != '.')
				{
					int num = board[i][j] - '1';
					if (rows[i][num]++) return false;
					if (cols[j][num]++) return false;
					if (blocks[i / 3][j / 3][num]++) return false;
				}
			}
		return true;
	}

};
