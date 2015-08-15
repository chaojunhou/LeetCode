//# include <stdio.h>
//# include <iostream>
//# include <vector>
//# include <string>
//# include <unordered_map>
//# include <cctype>
//# include <algorithm>
//# include <time.h>
//# include <queue>
//using namespace std;
//
//struct TreeNode {
//	int val;
//	TreeNode *left;
//	TreeNode *right;
//	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//};
//
//class Solution {
//public:
//	int sumNumbers(TreeNode* root)
//	{
//		int sum = 0;
//		if (root)		dfs(root, sum, 0);
//		return sum;
//	}
//	void dfs(TreeNode* root, int& sum, int ans)
//	{
//		ans = ans * 10 + root->val;
//		if (!root->left && !root->right)
//		{
//			sum += ans;
//			return;
//		}
//		if (root->left)			dfs(root->left, sum, ans);
//		if (root->right)		dfs(root->right, sum, ans);
//	}
//
//	void printTree(TreeNode* root)
//	{
//		if (root)
//		{
//			printTree(root->left);
//			cout << root->val;
//			printTree(root->right);
//		}
//	}
//};
//int  main()
//{
//	Solution sol;	
//	TreeNode *root1;
//	root1 = new TreeNode(4);
//	root1->left =new  TreeNode(2);
//	root1->right = new TreeNode(5);
//	root1->left->left = new TreeNode(1);
//	root1->left->right = new TreeNode(3);
//
//	cout << sol.sumNumbers(root1)<< endl;
//	//sol.printTree(root1);
//	cout<< endl;
//	system("pause");
//	return 0;
//}
//

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

	bool searchMatrix1(vector<vector<int>>& matrix, int target)
	{
		int row = matrix.size() - 1;
		//	cout<<row<<endl;
		int left = 0;
		int right = matrix[0].size() - 1;
		while (row >= 0 && matrix[row][0] > target) row--;
		if (row < 0)
			return false;
		while (left <= right)
		{
			int mid = (right - left) / 2 + left;
			if (matrix[row][mid] == target)
			{
				return true;
			}
			else if (matrix[row][mid] < target){
				left = mid + 1;
			}
			else{
				right = mid - 1;
			}
		}
		return false;
	}

	bool searchMatrix(vector<vector<int>>& matrix, int target)
	{
		int m = matrix.size();
		int n = matrix[0].size();
		int right = n*m - 1;
		int left = 0;
		while (left <= right)
		{
			int mid = (right - left) + left;
			if (matrix[mid / n][mid%n] == target)
			{
				return true;
			}
			else if (matrix[mid / n][mid%n] < target)
			{
				left = mid + 1;
			}
			else {
				right = mid - 1;
			}
		}
		return false;
	}
};


int main()
{
	Solution sol;
	vector<vector<int>> matrix = {
		{ 1, 3, 5, 7 },
		{ 10, 11, 16, 20 },
		{ 23, 30, 24, 50 },
	};

	int target = 2;
	//vector<vector<int>>	matrix = { { 1 } };
	//int	target = 0;
	cout << sol.searchMatrix(matrix, target) << endl;

	system("pause");
	return 0;
}


