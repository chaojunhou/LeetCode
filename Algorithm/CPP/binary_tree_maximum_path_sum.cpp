# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	int maxPathSum(TreeNode* root) 
	{
		int maxSum = INT_MIN;
		dfs(root, maxSum);
		return maxSum;
	}
	int dfs(TreeNode* root,int& maxSum)
	{
		if (root)
		{
			int left = dfs(root->left, maxSum);
			int right = dfs(root->right, maxSum);
			if ((left + right + root->val) > maxSum)
			{
				maxSum = left + right + root->val;
			}
			int res = max(left, right)+root->val;
			return (res > 0) ? res : 0;
		}
		return 0;
	}
};
int  main()
{
	Solution sol;
	TreeNode *root1;
	root1 = new TreeNode(4);
	root1->left = new  TreeNode(2);
	root1->right = new TreeNode(5);
	root1->left->left = new TreeNode(1);
	root1->left->right = new TreeNode(3);
	cout<<sol.maxPathSum(root1);
	cout << endl;
	system("pause");
	return 0;
}
