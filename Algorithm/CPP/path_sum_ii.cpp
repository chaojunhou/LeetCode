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
	vector<vector<int>> pathSum(TreeNode* root, int sum) 
	{
		vector<vector<int>> res;
		vector<int> ans;
		dfs(res, root, ans,0,sum);
		return res;
	}
	void dfs(vector<vector<int>>& res, TreeNode* root,  vector<int>ans,int tmp,int sum)
	{
		if (root)
		{
			tmp += root->val;
			ans.push_back(root->val);
			if (!root->left && !root->right)
			{
				if (tmp == sum)
				{
					res.push_back(ans);
					return;
				}
			}
			if (root->left)		dfs(res, root->left, ans,tmp,sum);
			if (root->right) dfs(res, root->right, ans,tmp,sum);
		}
		return;
	}
};
int  main()
{
	Solution sol;
	TreeNode *root1;
	root1 = new TreeNode(5);
	root1->left = new  TreeNode(4);
	root1->right = new TreeNode(8);
	root1->left->left = new TreeNode(11);
	root1->right->left = new TreeNode(13);
	root1->right->right = new TreeNode(4);
	root1->left->left->left = new TreeNode(7);
	root1->left->left->right = new TreeNode(2);
	root1->right->right->left =new TreeNode(5);
	root1->right->right->right = new TreeNode(1);
	for (auto k : sol.pathSum(root1,22))
	{
		for (auto x:k)
		cout << x << " ";
		cout << endl;
	}
	cout << endl;
	system("pause");
	return 0;
}
