# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
# include <vector>
# include <unordered_map>
# include <map>
using namespace std;

class Solution {
public:
	bool isValidSudoku(vector<vector<char>>& board) {
		int row = board.size();
		int col = board[0].size();
		vector<vector<int>> rows(9, vector<int>(9, 0));
		vector<vector<int>> cols(9, vector<int>(9, 0));
		vector<vector<vector<int>>> blocks(3, vector<vector<int>>(3, vector<int>(9, 0)));
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
