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
	vector<string> binaryTreePaths(TreeNode* root) {
		vector<string> res;
		string ans;
		dfs(res, root,ans);
		return res;
	}
	void dfs(vector<string>& res, TreeNode* root, string ans)
	{
		if (root)
		{
			ans += to_string(root->val);
			if (!root->left && !root->right)
			{
				res.push_back(ans);
				return;
			}
			ans += "->";
			if (root->left) dfs(res, root->left, ans);
			if (root->right) dfs(res, root->right, ans);
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
	//root1->right->left = new TreeNode(13);
	//root1->right->right = new TreeNode(4);
	//root1->left->left->left = new TreeNode(7);
	//root1->left->left->right = new TreeNode(2);
	//root1->right->right->left =new TreeNode(5);
	//root1->right->right->right = new TreeNode(1);
	for (auto k : sol.binaryTreePaths(root1))
	{
		cout << k << " ";
	}
	cout << endl;
	system("pause");
	return 0;
}
