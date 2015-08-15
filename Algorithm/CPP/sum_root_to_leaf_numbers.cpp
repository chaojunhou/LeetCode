# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
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
	int sumNumbers(TreeNode* root)
	{
		int sum = 0;
		if (root)		dfs(root, sum, 0);
		return sum;
	}
	void dfs(TreeNode* root, int& sum, int ans)
	{
		ans = ans * 10 + root->val;
		if (!root->left && !root->right)
		{
			sum += ans;
			return;
		}
		if (root->left)			dfs(root->left, sum, ans);
		if (root->right)		dfs(root->right, sum, ans);
	}

	void printTree(TreeNode* root)
	{
		if (root)
		{
			printTree(root->left);
			cout << root->val;
			printTree(root->right);
		}
	}
};
int  main()
{
	Solution sol;	
	TreeNode *root1;
	root1 = new TreeNode(4);
	root1->left =new  TreeNode(2);
	root1->right = new TreeNode(5);
	root1->left->left = new TreeNode(1);
	root1->left->right = new TreeNode(3);

	cout << sol.sumNumbers(root1)<< endl;
	//sol.printTree(root1);
	cout<< endl;
	system("pause");
	return 0;
}


