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
	vector<vector<int>> levelOrder(TreeNode* root) 
	{
		vector<vector<int>> res;
		dfs(res, root, 0);
		return res;
	}
	void dfs(vector<vector<int>> & res, TreeNode* root, int depth)
	{
		if (root)
		{
			if (res.size() == depth) // the new level, should build a new vector<int> to the res 
				 res.push_back(vector<int>());
			res[depth].push_back(root->val);
			dfs(res, root->left, depth + 1);
			dfs(res, root->right, depth + 1);
		}
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
	for (auto k : sol.levelOrder(root1))
	{
		for (auto x : k)
			cout << x << " ";
		cout << endl;
	}
	cout << endl;
	system("pause");
	return 0;
}
