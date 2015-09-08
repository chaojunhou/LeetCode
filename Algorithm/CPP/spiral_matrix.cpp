# include <iostream>
# include <string>
using namespace std;



class Solution {
public:
	vector<int> spiralOrder(vector<vector<int>>& matrix) {
		int m = matrix.size();
		vector<int> res;
		if (m < 1) return res;
		int n = matrix[0].size();
		int count = m*n;
		int up = 0;
		int down = m - 1;
		int left = 0;
		int right = n - 1;
		while (count)
		{
			for (int j = left; j <= right; j++)
			{
				res.push_back(matrix[up][j]);
				count--;
			}
			up++;
			if (count == 0) return res;
			for (int i = up; i <= down; i++)
			{
				res.push_back(matrix[i][right]);
				count--;
			}
			right--;
			if (count == 0) return res;
			for (int j = right; j >= left; j--)
			{
				res.push_back(matrix[down][j]);
				count--;
			}
			down--;
			if (count == 0) return res;
			for (int i = down; i >= up; i--)
			{
				res.push_back(matrix[i][left]);
				count--;
			}
			left++;
			if (count == 0) return res;
		}
		return res;
	}
};
int main()
{
	Solution sol;
	vector<int> nums = { 100, 4, 200, 1, 3, 2 };//4
	//nums = { 0, 0, -1 };//2
	//nums = { 1, 2, 0, 1 };//3
	vector<vector<int>> matrix = {
		{1,2,3},
		{4,5,6},
		{7,8,9}
	};
	matrix = { { 2, 3 } };
	for(auto k:sol.spiralOrder(matrix)) cout<<k<<" ";
	cout << endl;


	system("pause");
	return 0;

}
