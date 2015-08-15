# include <vector>
# include <algorithm>
# include <string>
# include <stack>
# include <algorithm>
# include <deque>
# include <iostream>
using namespace std;
class Solution {
public:
	bool searchMatrix1(vector<vector<int>>& matrix, int target) {
		int down= matrix.size();
		int i = 0;
		int j = matrix[0].size() - 1;
		while ((i < down) && (j >= 0))
		{
			if (matrix[i][j] == target)
			{
				return true;
			}
			else if (matrix[i][j] < target)
			{
				++i;
			}
			else
			{
				--j;
			}
		}
		return false;
	}
	/////////////////////////////////////
	bool binarySearch(vector<int>& vec, int target){
		int left = 0;
		int right = vec.size()-1;
		while (left <= right)
		{
			int mid = (right - left) / 2 + left;
			if (vec[mid] == target)
			{
				return true;
			}
			else if (vec[mid] < target)
			{
				left = mid +1;
			}
			else
			{
				right = mid - 1;
			}
		}
		return false;
	}
	bool searchMatrix(vector<vector<int>>& matrix, int target) {
		int down= matrix.size();
		int right = matrix[0].size()-1;
		int up = 0;
		cout << down << endl;
		cout << right << endl;
		while (up < down )
		{
			if (matrix[up][right] < target)
				up += 1;
			else
				break;
		}
		cout << "the value of up is " << up << endl;
		for (auto i = up; i < down; ++i)
		{
			if (binarySearch(matrix[i], target))
				return true;
		}
		return false;
	}
};


int main()
{
	Solution sol;
	//vector<vector<int>> matrix = { 
	//	{ 1, 4, 7, 11, 15 },
	//	{ 2, 5, 8, 12, 19 },
	//	{ 3, 6, 9, 16, 22 },
	//	{ 10, 13, 14, 17, 24 },
	//	{ 18, 21, 23, 26, 30 } 
	//};
	//
	//int target = 5;
	//cout << sol.searchMatrix(matrix, target) << endl;
	vector<vector<int>> matrix = { { -5 } };
	auto target = -5;
	cout << sol.searchMatrix(matrix, target);
	cin.get(); 
	return 0;
}


